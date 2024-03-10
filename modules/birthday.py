from modules.field import Field
from helpers.bot_utils import check_date


class Birthday(Field):
    def __init__(self, birthday="None"):
        birthday = check_date(birthday)
        self.birthday = birthday
        super().__init__(birthday)

    def __str__(self):
        return str(self.birthday)
