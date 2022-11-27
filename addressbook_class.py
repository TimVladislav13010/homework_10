from collections import UserDict


"""
Класи.
"""


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phones):
        self.phones.append(Phone(phones))

    def return_record(self):
        phone_numbers = ""
        for phone in self.phones:
            phone_numbers += f"{phone.value}"
        return f"{self.name.value}: {phone_numbers}"

    def change_phone_record(self, new_phone):

        if len(self.phones) == 0:
            self.phones.append(Phone(new_phone))

        if len(self.phones) == 1:
            self.phones[0].change_value(new_phone)

        if len(self.phones) > 1:
            i = -1
            print(f"Виберіть номер телефону для видалення")
            for phone in self.phones:
                i += 1
                print(f"№ {i} : {phone}")
            inp_user = int(input(f"Введіть №..."))
            self.phones[inp_user] = new_phone


class AddressBook(UserDict):
    """
    Книга контактів.
    """
    def add_record(self, record):
        self.data[record.name.value] = record

    def get_records(self):
        return self.data

    def get_name_record(self, name) -> Record:
        return self.data.get(name)


class Field:
    def __init__(self, value):
        self.value = value

    def change_value(self, new_value):
        self.value = new_value


class Name(Field):
    pass


class Phone(Field):
    pass
