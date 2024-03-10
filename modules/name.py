from modules.field import Field


class Name(Field):
    def __init__(self, name: str):
        name = name.capitalize()
        self.name = name
        super().__init__(name)

    def __str__(self):
        return str(self.name)
