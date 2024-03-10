from helpers.bot_utils import highlight, show_help
from helpers.bot_data_handler import load_from_json, save_to_json
import modules.bot_assistant as bot


def parse_input(user_input) -> str:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    print("\nWelcome to the assistant bot!")
    book = load_from_json()
    dirty = False
    
    while True:
        user_input = input("\nEnter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit", "bye"]:
            if dirty:
                save_to_json(book.to_json())
            print("Good bye!")
            break

        elif command in ["hello", "hi"]:
            print("How can I help you?")

        elif command == "add":
            dirty = True
            print(bot.add_contact(args, book))

        elif command == "change":
            dirty = True
            print(bot.change_contact(args, book))

        elif command == "rename":
            dirty = True
            print(bot.rename_contact(args, book))

        elif command == "remove":
            dirty = True
            print(bot.remove_contact(args, book))
        
        elif command == "remove-phone":
            dirty = True
            print(bot.remove_phone(args, book))

        elif command == "add-birthday":
            dirty = True
            print(bot.add_birthday(args, book))

        elif command == "show-birthday":
            print(bot.show_birthday(args, book))

        elif command == "birthdays":
            bot.birthdays(book)

        elif command == "phone":
            print(bot.show_phone(args, book))

        elif command == "all":
            print(bot.show_all(book))

        elif command in ["help", "?"]:
            print(show_help())

        else:
            print(
                f"Invalid command. Use {highlight("help")} or {highlight("?")} to see all available commands."
            )


if __name__ == "__main__":
    main()
