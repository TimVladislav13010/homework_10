from collections import UserDict


"""
Бот помічник.

Працює з командами (hello, add, change, phone, show_all, good_bye, close, exit, .)
"""


class AddressBook(UserDict):
    """
    Книга контактів.
    """


class Record:
    def add_record(self, name: str, phone: list) -> str:
        """
        Функція для додавання нового номеру в телефонну книгу
        """
        if name in AddressBook:
            return f"Цей контакт {name} вже використовується введіть інше ім`я"

        phone_number = (name, phone)
        AddressBook.update([phone_number])
        return f"Запис ({name} : {phone}) додано до словника"

    def del_record(self):
        pass

    def edit_record(self):
        pass


class Field:
    pass


class Name(Field):
    def __init__(self, name: str):
        self.name = name


class Phone(Field):
    def __int__(self, phone: list):
        self.phone = phone


def input_error(func):
    """
    Обробник помилок
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError:
            return f"Wrong command."
        except KeyError:
            return f"KeyError"
        except IndexError:
            return f"Wrong index"
        except ValueError:
            return f"ValueError"
    return wrapper


@input_error
def handler(commands):
    return USER_COMMANDS.get(commands, break_f)


def change_input(user_input):
    """
    Функція для обробки введених даних від користувача
    """
    new_input = user_input.split(" ")
    return new_input


def good_bye():
    return "Good Bye!"


def break_f():
    """
    Коли користувач введе щось інше крім команд повертається строка про неправильний ввід команди.
    """
    return f"Wrong enter... "


USER_COMMANDS = {
    # "hello": hello,
    "add": Record.add_record(),
    # "change": change,
    # "phone": phone,
    # "show_all": show_all,
    "good_bye": good_bye,
    "close": good_bye,
    "exit": good_bye,
    ".": good_bye
}


if __name__ == "__main__":
    while True:

        user_input = input("Введіть будь ласка команду "
                           "(hello, add, change, phone, show_all, good_bye, close, exit, .)")
        changes_commands = change_input(user_input)
        result = handler(changes_commands[0])

        if result == good_bye:
            print(result())
            break

        elif len(changes_commands) == 1: # or result == show_all or result == hello:
            result = handler(changes_commands[0])()
            print(result)

        elif len(changes_commands) == 2:
            result = handler(changes_commands[0])(changes_commands[1])
            print(result)

        elif len(changes_commands) == 3:
            result = handler(changes_commands[0])(changes_commands[1], changes_commands[2])
            print(result)

        elif len(changes_commands) > 3:
            result = f"({user_input}) - ви ввели невірну команду"
            print(result)

        continue
