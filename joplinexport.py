#!/usr/bin/env python3
import re
import sqlite3
from collections import defaultdict
from pathlib import Path
from shutil import copy
from shutil import rmtree
from typing import Optional


def slugify(text):
    return re.sub(r"[\W_]+", "-", text.lower()).strip("-")


class Note:
    def __init__(self, id, parent_id, parent_title, title, body):
        self.id = id
        self.parent_id = parent_id
        self.parent_title = parent_title
        self.title = title
        self.body = body

    def get_url(self):
        return slugify(self.parent_title) + "/" + slugify(self.title)


class JoplinExporter:
    content_dir = Path("content")
    static_dir = Path("static")
    joplin_dir = Path.home() / ".config/joplin-desktop"

    def clean_content_dir(self):
        """Reset the content directory to a known state to begin."""
        rmtree(self.content_dir)
        rmtree(self.static_dir)
        self.content_dir.mkdir()
        self.static_dir.mkdir()
        with open(self.content_dir / "_index.md", mode="w") as outfile:
            outfile.write('+++\nredirect_to = "welcome/stavros-notes/"\n+++')

    def resolve_note_links(self, note: Note) -> str:
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
        return resource_id + "." + resource[1]

    def copy_resources(self):
        """Copy all the resources to the output directory."""
        for resource_id, resource in self.resources.items():
            title, extension = resource
            copy(
                self.joplin_dir / "resources" / (f"{resource_id}.{extension}"),
                self.static_dir,
            )

    def read_data(self):
        """Read the data from the Joplin database."""
        conn = sqlite3.connect(self.joplin_dir / "database.sqlite")
        c = conn.cursor()

        # Create table
        c.execute("""SELECT id, title FROM folders;""")
        self.folders = {id: title for id, title in c.fetchall()}

        c.execute("""SELECT id, title, file_extension FROM resources;""")
        self.resources = {id: (title, ext) for id, title, ext in c.fetchall()}

        c.execute("""SELECT id, parent_id, title, body FROM notes;""")
        self.notes = defaultdict(list)
        self.note_lookup_dict = {}
        for id, parent_id, title, body in c.fetchall():
            note = Note(id, parent_id, self.folders[parent_id], title, body)
            self.notes[note.parent_id].append(note)
            self.note_lookup_dict[note.id] = note

        conn.close()

    def export(self):
        self.read_data()

        # Private notes shouldn't be published.
        folder_list = list(
            item for item in self.folders.items() if item[1] != "Private"
        )

        # Sort "Welcome" last.
        folder_list.sort(
            key=lambda x: x[1].lower().strip() if x[1] != "Welcome" else "0"
        )

        self.clean_content_dir()
        self.copy_resources()

        for folder_counter, folder in enumerate(folder_list, start=1):
            folder_id, folder_title = folder
            dir = self.content_dir / slugify(folder_title)
            dir.mkdir(parents=True)
            contents = []
            for note_counter, note in enumerate(
                sorted(self.notes[folder_id], key=lambda n: n.title)
            ):
                print(f"Exporting {folder_title} - {note.title}...")
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
{self.resolve_note_links(note)}"""
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


if __name__ == "__main__":
    print("Exporting Joplin database...")
    JoplinExporter().export()
