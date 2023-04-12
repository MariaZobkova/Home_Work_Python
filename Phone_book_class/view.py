from classes import Contact, PhoneBook
import text as txt


def main_menu():
    print('''Выберете команду по взаимодействию с телефонным справочником:
    1.Открыть файл
    2.Сохранить файл
    3.Посмотреть все контакты
    4.Создать контакт
    5.Найти контакт
    6.Редактировать контакт
    7.Удалить контакт
    8.Выход''')

    while True:
        choice = input('Введите команду: ')
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        else:
            print('Введите число от 1 до 8')

def print_info(message: str):
    print('\n' + '-' * len(message))
    print(message)
    print('-' * len(message) + '\n')


def show_contact(book: list[Contact], message: str):
    if book:
        for n, Contact in enumerate(book, 1):
            print(f'{n}. {Contact}')
    else:
        print(message)


def new_contact():
    print()
    name = input(txt.txt_name)
    phone = input(txt.txt_phone)
    comment = input(txt.txt_comment)
    print()
    return Contact(name, phone, comment)


def search_contact():
    print()
    search = input('Введите поисковый запрос: ')
    return search

def confirm(message: str):
    print()
    answer = input(message + 'yes/no')
    if answer == 'yes':
        return True
    else:
        return False






