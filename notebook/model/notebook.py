from dataclasses import dataclass, field
import datetime
import uuid
from typing import ClassVar


@dataclass
class Note:
    code: int
    text : str
    importance : str
    HIGH: ClassVar[str]= "HIGH"
    MEDIUM: ClassVar[str] = "MEDIUM"
    LOW:  ClassVar[str] = "LOW"
    tags: list[str] = field(init=False, default_factory=list)
    creation_time: datetime.datetime = field(default_factory=datetime.datetime.now)




    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
         return f" Code : {self.code}" \
                f" creation date : {self.creation_date}" \
                f" {self.title} : {self.text}"





class Notebook:
    def __init__(self):
        self.notes = dict[int, Note] = { }
        pass

    def add_note(self, title: str, text: str, importance: str):
        new_note = Note(title, text)
        new_note.code = str(uuid.uuid4())
        self.notes.append(new_note)
        return new_note.code
    def important_notes(self) -> list[Note]:
        importance_tag = []
        for x in self.tag :
            if x  == "HIGH" or "MEDIUM":
                x.append(importance_tag)
        return importance_tag

    def tags_note_count(self) -> dict[str, int]:
        dict_tags_count = {}
        for nota in self.notes:
            if nota.tag:
                for tag in nota.tag:
                    dict_tags_count[tag] = dict_tags_count.get(tag,0) + 1
        return dict_tags_count




















