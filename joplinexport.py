#!/usr/bin/env python3
import dataclasses
import mimetypes
import re
import sqlite3
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from shutil import copy
from shutil import rmtree
from typing import Dict
from typing import List
from typing import Optional
from typing import Set


def contains_word(word: str, text: str) -> bool:
    """
    Check whether `text` contains `word`, as a whole word.

    Case insensitive.
    """
    return re.search(f"\\b{word}\\b".lower(), text.lower()) is not None


def slugify(text):
    """Convert `text` into a slug."""
    return re.sub(r"[\W_]+", "-", text.lower()).strip("-")


@dataclasses.dataclass
class Note:
    """A helper type for a note."""

    id: str
    parent_id: str
    parent_title: str
    title: str
    body: str
    updated_time: datetime
    tags: List[str] = dataclasses.field(default_factory=list)

    def get_url(self):
        """Return the note's relative URL."""
        return slugify(self.parent_title) + "/" + slugify(self.title)


@dataclasses.dataclass
class Resource:
    """A helper type for a resource."""

    title: str
    # The actual extension that the file stored in Joplin has.
    extension: str
    mimetype: str

    @property
    def derived_ext(self):
        """Return an extension derived from the resource's mime type."""
        ext = mimetypes.guess_extension(self.mimetype, strict=False)
        return "" if ext is None else ext


class JoplinExporter:
    """The main exporter class."""

    content_dir = Path("content")
    static_dir = Path("static/resources")
    joplin_dir = Path.home() / ".config/joplin-desktop"

    def __init__(self):
        self.resources: Dict[str, Resource] = {}
        self.used_resources: Set[str] = set()

    def clean_content_dir(self):
        """Reset the content directory to a known state to begin."""
        rmtree(self.content_dir)
        rmtree(self.static_dir)
        self.content_dir.mkdir()
        self.static_dir.mkdir()
        with open(self.content_dir / "_index.md", mode="w") as outfile:
            outfile.write('+++\nredirect_to = "welcome/stavros-notes/"\n+++')

    def resolve_note_links(self, note: Note) -> str:
        """Resolve the links between notes and replace them in the body."""

        def replacement(match):
            item_id = match.group(1)
            new_url = self.get_note_url_by_id(item_id)
            if not new_url:
                new_url = self.get_resource_url_by_id(item_id)
                if not new_url:
                    new_url = item_id
            return f"](../../{new_url})"

        return re.sub(r"\]\(:/([a-f0-9]{32})\)", replacement, note.body)

    def get_note_url_by_id(self, note_id: str) -> Optional[str]:
        """Return a note's relative URL by its ID."""
        note = self.note_lookup_dict.get(note_id)
        if not note:
            return None
        return note.get_url()

    def get_resource_url_by_id(self, resource_id: str) -> Optional[str]:
        """Return a resource's relative URL by its ID."""
        resource = self.resources.get(resource_id)
        if not resource:
            return None
        # Add the resource to the set of used resources, so we can only copy
        # the resources that are used.
        self.used_resources.add(resource_id)
        return "resources/" + resource_id + resource.derived_ext

    def copy_resources(self):
        """Copy all the used resources to the output directory."""
        for resource_id in self.used_resources:
            resource = self.resources[resource_id]
            copy(
                self.joplin_dir / "resources" / (f"{resource_id}.{resource.extension}"),
                self.static_dir / f"{resource_id}{resource.derived_ext}",
            )

    def read_data(self):
        """Read the data from the Joplin database."""
        conn = sqlite3.connect(self.joplin_dir / "database.sqlite")
        c = conn.cursor()

        c.execute("""SELECT id, title FROM folders;""")
        self.folders = {id: title for id, title in c.fetchall()}

        # Get the tags by ID.
        c.execute("""SELECT id, title FROM tags;""")
        tags = {id: title for id, title in c.fetchall()}
        # Get the tag IDs for each note ID.
        c.execute("""SELECT note_id, tag_id FROM note_tags;""")
        note_tags = defaultdict(list)
        for note_id, tag_id in c.fetchall():
            note_tags[note_id].append(tags[tag_id])

        c.execute("""SELECT id, title, mime, file_extension FROM resources;""")

        self.resources = {
            id: Resource(
                title=title,
                extension=ext,
                mimetype=mime,
            )
            for id, title, mime, ext in c.fetchall()
        }

        c.execute("""SELECT id, parent_id, title, body, updated_time FROM notes;""")
        self.notes = defaultdict(list)
        self.note_lookup_dict = {}
        for id, parent_id, title, body, updated_time in c.fetchall():
            note = Note(
                id,
                parent_id,
                self.folders[parent_id],
                title,
                body,
                datetime.fromtimestamp(updated_time / 1000),
                tags=note_tags[id],
            )
            self.notes[note.parent_id].append(note)
            self.note_lookup_dict[note.id] = note

        conn.close()

    def export(self):
        """Export all the notes to a static site."""
        self.read_data()

        # Private notes shouldn't be published.
        folder_list = list(
            i for i in self.folders.items() if not contains_word("private", i[1])
        )

        # Sort "Welcome" last.
        folder_list.sort(
            key=lambda x: x[1].lower().strip() if x[1] != "Welcome" else "0"
        )

        self.clean_content_dir()

        for folder_counter, folder in enumerate(folder_list, start=1):
            folder_id, folder_title = folder
            dir = self.content_dir / slugify(folder_title)
            dir.mkdir(parents=True)
            contents = []
            note_counter = 0
            for note in sorted(self.notes[folder_id], key=lambda n: n.title):
                if (
                    contains_word("private", note.title)
                    or contains_word("wip", note.title)
                    or "wip" in note.tags
                    or "private" in note.tags
                ):
                    print(
                        f"Note is unpublished, skipping: {folder_title} - {note.title}."
                    )
                    continue

                print(f"Exporting {folder_title} - {note.title}...")
                note_counter += 1
                contents.append((note.title, note.get_url()))
                with (self.content_dir / (note.get_url() + ".md")).open(
                    mode="w"
                ) as outfile:
                    outfile.write(
                        f"""+++
title = "{note.title}"
weight = {note_counter}
sort_by = "weight"
insert_anchor_links = "right"
+++
{self.resolve_note_links(note)}

* * *

<p style="font-size:80%; font-style: italic">
Last updated on {note.updated_time:%B %d, %Y}. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
"""
                    )

            with (dir / "_index.md").open(mode="w") as outfile:
                contents_list = "\n1. ".join(
                    f"[{title}](../../{url})" for title, url in contents
                )
                outfile.write(
                    f"""+++
title = "{folder_title}"
weight = {folder_counter}
sort_by = "weight"
insert_anchor_links = "right"
+++
## Contents

Click on a link in the list below to go to that page:

1. {contents_list}
"""
                )

        self.copy_resources()


if __name__ == "__main__":
    print("Exporting Joplin database...")
    JoplinExporter().export()
