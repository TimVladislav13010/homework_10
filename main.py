from collections import UserDict


"""
Бот помічник.
Працює з командами (hello, add, change, phone, show_all, good_bye, close, exit, .)
"""

ADDRESSBOOK = {"Vlad": ["0687417002"]}


class AddressBook(UserDict):
    """
    Книга контактів.
    """


class Record:
    pass


class Field:
    pass


class Name(Field):
    pass


class Phone(Field):
    pass


if __name__ == "__main__":
    user_1 = AddressBook(AddressBook)
    print(user_1)
