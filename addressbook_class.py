from collections import UserDict


"""
Класи.
"""


class Record:
    def __init__(self, names):
        self.name = Name(names)
        self.phones = []

    def add_phone(self, phones):
        self.phones.append(Phone(phones))


class AddressBook(UserDict):
    """
    Книга контактів.
    """
    def add_record(self, record):
        self.data[record.name.value] = record

    def get_record(self):
        return self.data


class Field:
    def __int__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass
