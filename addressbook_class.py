from collections import UserDict


"""
Класи.
"""


class AddressBook(UserDict):
    """
    Книга контактів.
    """
    def add_record(self, record):
        self.data[record.name.value] = record

    def get_record(self):
        return self.data


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phone = []

    def add_record(self):
        AddressBook.add_record(self.name)

    def add_phone(self, phone):
        self.phone.append(Phone(phone))


class Field:
    def __int__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass
