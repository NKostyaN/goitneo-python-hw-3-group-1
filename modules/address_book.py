from collections import UserDict
from modules.record import Record


class AddressBook(UserDict):
    def __init__(self):
        self.data = UserDict()

    def add_record(self, record: Record):
        self.data.update({str(record.name): record})

    def delete(self, record: str):
        self.data.pop(record)

    def find(self, name: str) -> Record:
        return self.data.get(name)

    def to_json(self) -> dict:
        res = {}
        for key in self.data.keys():
            res.update({key: self.data.get(key).to_json()})
        return res
