from addressbook_class import AddressBook, Record


"""
Бот помічник.
Працює з командами (hello, add, change, phone, show_all, good_bye, close, exit, .)
"""


PHONE_BOOK = AddressBook()


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
def change_input(user_input):
    """
    Функція для обробки введених даних від користувача
    """
    new_input = user_input
    data = ''
    for key in USER_COMMANDS:
        if user_input.strip().lower().startswith(key):
            new_input = key
            data = user_input[len(new_input):]
            break
    if data:
        return handler(new_input)(data)
    return handler(new_input)()


def hello():
    return "How can I help you?"


@input_error
def add(data):
    """
    Функція для додавання нового номеру в телефонну книгу
    """
    name, phones = create_data(data)
    print(name, phones)
    print(PHONE_BOOK)
    if name in PHONE_BOOK:
        return f"Цей контакт {name} вже використовується введіть інше ім`я"
    record = Record(name)
    record.add_phone(phones)
    PHONE_BOOK.add_record(record)
    return f"Запис ({name} : {phones}) додано до словника"


@input_error
def create_data(data):
    """
    Розділяє вхідні дані - номер і телефон.
    """
    name, phones = data.strip().split(' ')

    if name.isnumeric():
        raise ValueError('Wrong name.')
    for phon in phones:
        if not phon.isnumeric():
            raise ValueError('Wrong phones.')
    return name.title(), phones


@input_error
def change(name, number):
    """
    Функціця для змінни існуючого номеру в телефонній книзі
    """
    if name not in PHONE_BOOK:
        return f"{name} імя не знайдено в словнику"

    elif not number.isdigit():
        return f"{number} не числово будь ласка введіть числа"

    PHONE_BOOK[name] = number

    return f"Запис ({name} : {number}) замінено в словнику"


def phone(name):
    """
    Функція повертає номер телефону з телефонної книги
    """
    if not PHONE_BOOK.get(name):
        return f"{name} не знайдено в телефонній книзі"
    phones = PHONE_BOOK.get(name)
    return f"{name} : {phones}"


def show_all():
    """
    Функція для відображення всієї телефонної книги
    """
    show_number = ""
    for key, val in PHONE_BOOK.items():
        show_number += "Ім'я: " + key + ", номер: " + val + "\n"
    return show_number


def good_bye():
    return "Good Bye!"


def break_f():
    """
    Коли користувач введе щось інше крім команд повертається строка про неправильний ввід команди.
    """
    return f"Wrong enter... "


@input_error
def handler(commands):
    return USER_COMMANDS.get(commands, break_f)


USER_COMMANDS = {
    "hello": hello,
    "add": add,
    "change": change,
    "phone": phone,
    "show_all": show_all,
    "good_bye": good_bye,
    "close": good_bye,
    "exit": good_bye,
    ".": good_bye
}


def main():
    """
    Логіка роботи бота помічника
    """
    while True:
        user_input = input("Введіть будь ласка команду "
                           "(hello, add, change, phone, show_all, good_bye, close, exit, .)")
        result = change_input(user_input)
        print(result)
        if result == "Good Bye!":
            break


if __name__ == "__main__":
    main()
