phone_book = []
start_phone_book = []
PATH = 'phone_book.txt'


class Contact:

    def __init__(self, name: str, phone: str, comment: str = ''):
        self.name = name
        self.phone = phone
        self.comment = comment

    def contact_to_str(self):
        return f'{self.name} ; {self.phone} ; {self.comment}'

    def __str__(self):
        return f'{self.name} : {self.phone} : {self.comment}'


class PhoneBook:

    def __init__(self, PATH: str):
        self.PATH = PATH
        self.phone_book: list[Contact] = []
        self.is_shanged = False

    def load(self):
        self.phone_book.clear()
        with open(self.PATH, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            contact = contact.strip().split(';')
            self.phone_book.append(Contact(contact[0], contact[1], contact[2]))



    def save(self):
        data = []
        for contact in self.phone_book:
            data.append(contact.contact_to_str())
            data = '\n'.join(data)
        with open(PATH, 'w', encoding='UTF-8') as file:
            file.write(data)
        self.is_shanged = False


    def get(self):
        return self.phone_book



    def add(self, contact: Contact):
        self.phone_book.append(contact)
        self.is_shanged = True

    def find(self, name_contact: str):
        data = []
        for contact in self.phone_book:
            if name_contact in contact.contact_to_str():
                data.append(contact)
        return data


    def edit(self, previous_version: list[Contact], present_version: Contact):
        for contact in self.phone_book:
            for option in previous_version:
                if contact == option:
                    self.phone_book.remove(contact)
        self.phone_book.append(present_version)
        self.is_shanged = True
        return self.phone_book


    def delete(self, remove_contact: list[Contact]):
        for contact in self.phone_book:
            for option in remove_contact:
                if contact == option:
                    self.phone_book.remove(contact)
        self.is_shanged = True
        return self.phone_book

    def exit(self):
        if self.phone_book == self.original_book:
            return False
        else:
            return True

    def save_on_exit(self):
        return self.is_shanged

