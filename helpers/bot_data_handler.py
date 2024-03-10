import json
from helpers.bot_utils import info
from modules.address_book import AddressBook
from modules.record import Record


def load_from_json() -> AddressBook:
    phonebook = AddressBook()
    try:
        with open("phonebook.json", "r", encoding="utf-8 ") as f:
            data = json.load(f)
            if data != "":
                for key in data.keys():
                    rec = Record(key)
                    for phone in data.get(key).get("phones"):
                        rec.add_phone(phone)
                    if str(data.get(key).get("birthday")) != "None":
                        rec.add_birthday(data.get(key).get("birthday"))
                    phonebook.add_record(rec)
            else:
                Log.empty()
    except FileNotFoundError:
        Log.not_found()
    return phonebook


def save_to_json(data: dict):
    with open("phonebook.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


class Log:
    def empty():
        return print(info("[INFO]: Phonebook file found, but it's empty for now."))

    def not_found():
        return print(
            info(
                "[INFO]: Phonebook file not found, but don't worry, I'll create a new one for you."
            )
        )
