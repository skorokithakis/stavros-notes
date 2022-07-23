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
from typing import Union


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
class Folder:
    """A helper type for a folder."""

    id: str
    parent_id: str
    title: str

    def is_private(self) -> bool:
        """Return whether this folder is private."""
        return contains_word("private", self.title)

    def get_url(self) -> str:
        """Return the folder's relative URL."""
        return slugify(self.title)

    def get_summary_line(self, level: int) -> str:
        """Get the appropriate summary file line for this folder."""
        return ("    " * (level - 1)) + f"- [{self.title}]({self.get_url()}/index.md)"

    def __lt__(self, other: Union["Folder", "Note"]) -> bool:
        """Support comparison, for sorting."""
        if isinstance(other, Note):
            # Folders always come before notes.
            return True
        return self.title.lower() < other.title.lower()

    def __repr__(self) -> str:
        """Pretty-print this class."""
        return f"Folder: <{self.title}>"


@dataclasses.dataclass
class Note:
    """A helper type for a note."""

    id: str
    folder: Folder
    title: str
    body: str
    updated_time: datetime
    tags: List[str] = dataclasses.field(default_factory=list)

    def is_private(self) -> bool:
        """
        Check whether a note is private.

        This function checks a note's title and tags and returns whether it
        should be considered private or whether it should be published.
        """
        hidden_keywords = ["private", "wip", "draft"]
        for keyword in hidden_keywords:
            if contains_word(keyword, self.title) or keyword in self.tags:
                return True
        return False

    def get_url(self) -> str:
        """Return the note's relative URL."""
        return slugify(self.folder.title) + "/" + slugify(self.title)

    def get_summary_line(self, level: int) -> str:
        """
        Get the appropriate summary file line for this note.

        The introduction is level 0, and is treated differently here.
        """
        return (
            "    " * (level - 1)
        ) + f"{'- ' if level > 0 else ''}[{self.title}]({self.get_url()}.md)"

    def __lt__(self, other: Union["Folder", "Note"]) -> bool:
        """Support comparison, for sorting."""
        return self.title.lower() < other.title.lower()

    def __repr__(self) -> str:
        """Pretty-print this class."""
        return f"Note: <{self.title}>"


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

        # A mapping of {"note_id": Note()}.
        self.note_lookup_dict: Dict[str, Note] = {}

        # A mapping of {"folder_id": Folder()}.
        self.folders: Dict[str, Folder] = {}

        # A mapping of {"folder_id": [Note(), Note()]}.
        self.notes: Dict[str, List[Note]] = defaultdict(list)

    def clean_content_dir(self):
        """Reset the content directory to a known state to begin."""
        rmtree(self.content_dir, ignore_errors=True)
        rmtree(self.static_dir, ignore_errors=True)
        self.content_dir.mkdir(parents=True)
        self.static_dir.mkdir(parents=True)

    def resolve_note_links(self, note: Note) -> str:
        """Resolve the links between notes and replace them in the body."""

        def replacement(match):
            item_id = match.group(1)
            new_url = self.get_note_url_by_id(item_id)
            if new_url:
                new_url += ".html"
            else:
                new_url = self.get_resource_url_by_id(item_id)
                if not new_url:
                    new_url = item_id
            if match.group(2):
                new_url += match.group(2)
            return f"](/{new_url})"

        return re.sub(r"\]\(:/([a-f0-9]{32})(#.*?)?\)", replacement, note.body)

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

        c.execute("""SELECT id, title, parent_id FROM folders;""")
        self.folders = {
            id: Folder(id, parent_id, title) for id, title, parent_id in c.fetchall()
        }

        self.folders = {
            id: folder for id, folder in self.folders.items() if not folder.is_private()
        }

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
        for id, parent_id, title, body, updated_time in c.fetchall():
            if parent_id not in self.folders:
                # This note is in a private folder, continue.
                continue

            note = Note(
                id,
                self.folders[parent_id],
                title,
                body,
                datetime.fromtimestamp(updated_time / 1000),
                tags=note_tags[id],
            )
            if note.is_private():
                continue

            self.notes[note.folder.id].append(note)
            self.note_lookup_dict[note.id] = note

        conn.close()

    def write_summary(self):
        """Write the SUMMARY.md that mdBook needs."""
        # We construct a note tree by adding each note into its parent.
        note_tree: Dict[str, List[Union[Note, Folder]]] = defaultdict(list)

        # The note tree is a list of notes with their parents:
        # [
        #     [parent1, parent2, note1]
        #     [parent1, parent3, note2]
        # ]
        # Then, we sort these by alphabetical order, and we're done.
        note_tree = []
        introduction: Optional[Note] = None  # The "introduction" note.
        folders: List[Folder] = list
        for note_list in self.notes.values():
            for note in note_list:
                if note.folder.title == "Welcome":
                    introduction = note
                    continue
                note_item = [note]
                item: Union[Folder, Note] = note
                while True:
                    if isinstance(item, Note):
                        item = item.folder
                    elif isinstance(item, Folder):
                        item = self.folders.get(item.parent_id)
                        if not item:
                            break
                    note_item.insert(0, item)

                # Append the folders to the list if they weren't there before, as that's
                # the only way this algorithm can generate headlines.
                if folders != note_item[:-1]:
                    folders = note_item[:-1]
                    note_tree.append(folders)

                note_tree.append(note_item)
        note_tree.sort()

        # Generate the summary file.
        items = []
        for note_list in note_tree:
            level = len(note_list)
            if isinstance(note_list[-1], Folder):
                # The last item in the list is a folder, which means this is a header.
                items.append(note_list[-1].get_summary_line(level))
            else:
                # This is a regular note.
                note = note_list[-1]
                print(f"Exporting {note.title}...")
                items.append(note.get_summary_line(level))

        with (self.content_dir / "SUMMARY.md").open("w") as outfile:
            outfile.write("# Summary\n\n")
            # Special-case the introduction.
            if introduction:
                outfile.write(introduction.get_summary_line(0) + "\n")
            outfile.write("\n".join(items))

    def export(self):
        """Export all the notes to a static site."""
        self.read_data()

        folder_list = sorted(self.folders.values())

        self.clean_content_dir()

        for folder in folder_list:
            contents = []
            dir = self.content_dir / folder.get_url()
            dir.mkdir(parents=True, exist_ok=True)
            for note in sorted(self.notes[folder.id], key=lambda n: n.title):
                print(f"Exporting {folder.title} - {note.title}...")
                contents.append((note.title, f"{note.get_url()}.html"))
                with (self.content_dir / (note.get_url() + ".md")).open(
                    mode="w", encoding="utf-8"
                ) as outfile:
                    outfile.write(
                        f"""# {note.title}

{self.resolve_note_links(note)}

* * *

<p style="font-size:80%; font-style: italic">
Last updated on {note.updated_time:%B %d, %Y}. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
"""
                    )

            with (dir / "index.md").open(mode="w") as outfile:
                contents_list = "\n1. ".join(
                    f"[{title}](../../{url})" for title, url in contents
                )
                outfile.write(
                    f"""# Contents

Click on a link in the list below to go to that page:

1. {contents_list}
"""
                )

        self.write_summary()
        self.copy_resources()


if __name__ == "__main__":
    print("Exporting Joplin database...")
    JoplinExporter().export()
