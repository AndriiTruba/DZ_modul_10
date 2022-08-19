from collections import UserDict


class Field:

    def __init__(self, value: str) -> None:
        self.value = value

class Name(Field):

    def __init__(self, value: str) -> None:
        super().__init__(value)

class Phone(Field):
    def __init__(self, value: str) -> None:
        super().__init__(value)


class Record:

    def __init__(self, name: Name, phone: Phone = None):
        self.name: Name = name
        self.phones: list[Phone] = [phone] if phone is not None else []

    def add_phone(self, phone_number: Phone):
        self.phones.append(phone_number)

    def change_phone(self, old_number: Phone, new_number: Phone):
        try:
            self.phones.remove(old_number)
            self.phones.append(new_number)
        except ValueError:
            return f'{old_number} does not exists'

    def delete_contact(self, phone: Phone):
        try:
            self.phones.remove(phone)
        except ValueError:
            return f'{phone} is not exists'
    

class AddressBook(UserDict):
    
    def add_contact(self, name: Name, phone: Phone = None):
        contact = Record(name, phone)
        self.data[name.value] = contact

    def add_record(self, record: Record):
        self.data[record.name.value] = record


