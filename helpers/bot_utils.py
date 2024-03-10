from datetime import datetime, timedelta


def highlight(txt: str) -> str:
    return f"\033[96m{txt}\x1b[0m"          # cyan

def warning(txt: str) -> str:
    return f"\033[91m{txt}\x1b[0m"          # red

def info(txt: str) -> str:
    return f"\33[90m{txt}\x1b[0m"          # grey

def error(txt: str) -> str:
    return f"\033[41m{txt}\x1b[0m"          # red background

def strip_phone_number(phone: str, digits=10) -> str:
    phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("+", "")
        .replace("-", "")
        .replace("=", "")
        .replace("_", "")
        .replace("*", "")
        .replace("/", "")
        .replace("|", "")
        .replace(" ", "")
    )
    if len(phone) > digits:
        phone = phone[-digits : len(phone)]
    return phone


def show_help() -> str:
    help = (
        "\nAvailable commands:\n"
        f"{highlight("add [username] [phone]")} - adding contact to the phonebook or adding new phone to existing contact\n"
        f"{highlight("change [username] [old phone] [new phone]")} - changing contact in the phonebook\n"
        f"{highlight("rename [username] [new phone]")} - rename contact in the phonebook\n"
        f"{highlight("remove [username]")} - remove contact from phonebook\n"
        f"{highlight("remove-phone [username] [phone]")} - remove phone from contact\n"
        f"{highlight("phone [username]")} - show all phones of contact\n"
        f"{highlight("add-birthday [username] [birthday]")} - adding birthday of contact in {highlight("DD.MM.YYYY")} format\n"
        f"{highlight("show-birthday [username]")} - show birthday of the contact\n"
        f"{highlight("birthdays")} - show all contacts with birthdays on next week\n"
        f"{highlight("all")} - show all contacts in phonebook\n"
        f"{highlight("close")}, {highlight("exit")}, {highlight("quit")}, {highlight("bye")} - close application\n"
        f"{highlight("hello")}, {highlight("hi")} - just a greeting\n"
        f"{highlight("help")}, {highlight("?")} - this help"
    )
    return help


def check_date(date_str: str) -> str:
    date_format = "%d.%m.%Y"
    date = ""
    try:
        date = datetime.strftime(datetime.strptime(date_str, date_format), date_format)
        return date
    except Exception as e:
        print(f"{warning(f"Error in {check_date.__name__}:")} {e}")
        print(f"Use {highlight("DD.MM.YYYY")} format please\n")
    
    

def get_birthdays_per_week(users: list) -> str:
    today = datetime.today().date()
    weekdays = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": [],
    }
    try:
        for usr in users:
            for key in usr.keys():
                name = key
                bday = datetime.strptime(usr[key], "%d.%m.%Y").date()
            bday_this_year = bday.replace(year=today.year)

            if bday_this_year < today:
                if bday_this_year.weekday() < 5 or (
                    today.weekday() != 0 and today.weekday() != 6
                ):
                    bday_this_year = bday_this_year.replace(
                        year=bday_this_year.year + 1
                    )

            weekday = bday_this_year.weekday()
            if weekday >= 5:
                bday_this_year += timedelta(days=7 - weekday)

            delta = (bday_this_year - today).days
            if delta < 7:
                weekdays[bday_this_year.strftime("%A")].append(name)

        bdays = {}
        for k, v in weekdays.items():
            if v != []:
                bdays.update({k: v})
        if bdays != {}:
            for k, v in bdays.items():
                print(f"{highlight(str(k))}: {", ".join(v)}")
        else:
            print("There is no one to congratulate during the week")

    except TypeError:
        print(error("Something wrong in input data, pls check it"))


if __name__ == "__main__":
    pass
