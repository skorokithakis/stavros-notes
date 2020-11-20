#!/usr/bin/env python3
import re
import sqlite3
from collections import defaultdict
from pathlib import Path
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

    def clean_content_dir(self):
        """Reset the content directory to a known state to begin."""
        rmtree(self.content_dir)
        self.content_dir.mkdir()
        with open(self.content_dir / "_index.md", mode="w") as outfile:
            outfile.write('+++\nredirect_to = "welcome"\n+++')

    def resolve_note_links(self, note: Note) -> str:
        def replacement(match):
            note_id = match.group(1)
            new_url = self.get_note_url_by_id(note_id)
            return "](" + ("../../" + new_url if new_url else note_id) + ")"

        return re.sub(r"\]\(:/([a-f0-9]{32})\)", replacement, note.body)

    def get_note_url_by_id(self, note_id: str) -> Optional[str]:
        """Return a note's relative URL by its ID."""
        note = self.note_lookup_dict.get(note_id)
        if not note:
            return None
        return note.get_url()

    def read_data(self):
        conn = sqlite3.connect(Path.home() / ".config/joplin-desktop/database.sqlite")
        c = conn.cursor()

        # Create table
        c.execute("""SELECT id, title FROM folders;""")
        self.folders = {id: title for id, title in c.fetchall()}

        c.execute("""SELECT id, title FROM resources;""")
        self.resources = {id: title for id, title in c.fetchall()}

        c.execute("""SELECT id, parent_id, title, body FROM notes;""")
        self.notes = defaultdict(list)
        self.note_lookup_dict = {}
        for id, parent_id, title, body in c.fetchall():
            note = Note(id, parent_id, self.folders[parent_id], title, body)
            self.notes[note.parent_id].append(note)
            self.note_lookup_dict[note.id] = note

        conn.close()

    def export(self):
        folder_list = list(self.folders.items())
        # Sort "Welcome" last.
        folder_list.sort(
            key=lambda x: x[1].lower().strip() if x[1] != "Welcome" else "0"
        )

        outdir = Path.cwd() / "content"
        self.clean_content_dir()

        for counter, folder in enumerate(folder_list, start=1):
            folder_id, folder_title = folder
            dir = outdir / slugify(folder_title)
            dir.mkdir(parents=True)
            with (dir / "_index.md").open(mode="w") as outfile:
                outfile.write(
                    f"""+++
title = "{folder_title}"
weight = {counter}
sort_by = "weight"
insert_anchor_links = "right"
+++
Select one of the sublinks on the left to see the notes in this section."""
                )

            for counter, note in enumerate(
                sorted(self.notes[folder_id], key=lambda n: n.title)
            ):
                print(f"Exporting {folder_title} - {note.title}...")
                with (outdir / (note.get_url() + ".md")).open(mode="w") as outfile:
                    outfile.write(
                        f"""+++
title = "{note.title}"
weight = {counter}
sort_by = "weight"
insert_anchor_links = "right"
+++
{self.resolve_note_links(note)}"""
                    )


if __name__ == "__main__":
    print("Exporting Joplin database...")
    exporter = JoplinExporter()
    exporter.read_data()
    exporter.export()
