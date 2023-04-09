phone_book = []
start_phone_book = []
PATH = 'phone_book.txt'


def get_phone_book():
    global phone_book
    return phone_book
def load_file():
    global phone_book
    global start_phone_book
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(':')
        phone_book.append({'name': contact[0],
                           'phone': contact[1],
                           'comment': contact[2]})
    start_phone_book = phone_book.copy()

def save_file():
    global phone_book
    data = []
    for contact in phone_book:
        data.append(':'.join([value for value in contact.values()]))
        data = '\n'.join(data)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data)

def add_contact(contact: dict):
    global phone_book
    phone_book.append(contact)


def find_contact(name_contact: str):
    global phone_book
    data = []
    for contact in phone_book:
        if name_contact in contact.values():
            data.append(contact)
    return data

def edit_contact(previous_version: list, present_version: dict):
    global phone_book
    for contact in phone_book:
        for option in previous_version:
            if contact == option:
                phone_book.remove(contact)
    phone_book.append(present_version)
    return phone_book

def delete_contact(remove_contact: list):
    global phone_book
    for contact in phone_book:
        for option in remove_contact:
            if contact == option:
                phone_book.remove(contact)
    return phone_book

def exit_pb():
    global phone_book, start_phone_book
    if phone_book == start_phone_book:
        return False
    else:
        return True


