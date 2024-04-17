from dataclasses import dataclass, field
from _datetime import datetime
from typing import ClassVar


@dataclass
class Note:
    code: int
    text: str
    importance: str
    HIGH: ClassVar[str] = "HIGH"
    MEDIUM: ClassVar[str] = "MEDIUM"
    LOW:  ClassVar[str] = "LOW"
    tags: list[str] = field(init=False, default_factory=list)
    creation_date: datetime = field(init=False, default_factory=datetime.now)




    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
         return f" Code : {self.code}\nCreation date: {self.creation_date}\n{self.title}: {self.text}"






class Notebook:
    def __init__(self):
        self.notes = dict[int, Note] = {}


    def add_note(self, title: str, text: str, importance: str):
        code: int = len(self.notes) + 1
        note: Note = Note(code, title, text, importance)
        self.notes[code] = note
        return code

    def important_notes(self) -> list[Note]:
        return [note for note in self.notes.values() if note.importance == Note.HIGH or note.importance == Note.MEDIUM]


    def tags_note_count(self) -> dict[str, int]:
        tags_count = {}
        for note in self.notes.values():
            for tag in note.tags:
                if tag not in tags_count:
                    tags_count[tag] = 1
                else:
                    tags_count[tag] += 1
        return tags_count




















