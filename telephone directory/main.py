print('Доброго времени суток! Выберете команду по взаимодействию с телефонным справочником: ')
print('1 - Открыть файл')
print('2 - Сохранить файл')
print('3 - Посмотреть все контакты')
print('4 - Создать контакт')
print('5 - Найти контакт')
print('6 - Редактировать контакт')
print('7 - Удалить контакт')
print('8 - Выход')
def open_contacts():
    file = open('contacts.txt', 'r', encoding='utf-8')
    data = file.readlines()
    for i in data:
        print(i)
    file.close()

def create_contact():
    file = open('contacts.txt', 'a', encoding='utf-8')
    add_contact = input('Введите данные контакта: ')
    file.writelines('\n')
    file.writelines(add_contact)
    file.close()

def find_contact():
    file = open('contacts.txt', 'r', encoding='utf-8')
    query = input('Введите данные контакта для поиска: ')
    data = file.readlines()
    for i in data:
        if query in i:
            print(i)
    else: print('Такого контакта нет')
    file.close()

def edit_contact():
    file = open('contacts.txt', 'r', encoding='utf-8')
    data = file.readlines()
    file.close()
    query = input('Введите данные контакта для редактирования: ')
    count = 0
    for i in data:
        if query in i:
            print(i)
            count +=1
            result_contact = i
    if count == 0:
        print('Такого контакта нет')
    if count == 1:
        data.remove(result_contact)
        data.append(input('\nВведите новую редакцию контакта:'))
        file = open('contacts.txt', 'w', encoding='utf-8')
        for i in data:
            file.writelines(i)
        file.close()
    elif count != 1 and count != 0:
        print('Выберите контакт из списка совпадений и еще раз введите его полные данные')
        edit_contact()

def remove_contact():
    file = open('contacts.txt', 'r', encoding='utf-8')
    data = file.readlines()
    file.close()
    query = input('Введите данные контакта для удаления: ')
    count = 0
    for i in data:
        if query in i:
            print(i)
            count +=1
            result_contact = i
    if count == 0:
        print('Такого контакта нет')
    if count == 1:
        data.remove(result_contact)
        file = open('contacts.txt', 'w', encoding='utf-8')
        for i in data:
            file.writelines(i)
        file.close()
    elif count != 1 and count != 0:
        print('Выберите контакт из списка совпадений и еще раз введите его полные данные')
        remove_contact()



action = int(input('Введите номер команды: '))
if action == 1:
    file = open('contacts.txt', 'r', encoding='utf-8')
    data = file.readlines()
    print(data)
    file.close()
elif action == 3:
    open_contacts()
elif action == 4:
    create_contact()
elif action == 5:
    find_contact()
elif action == 6:
    edit_contact()
elif action == 7:
    remove_contact()
elif action == 8:
    file = open('contacts.txt', 'r', encoding='utf-8')
    file.close()





# data = open('contacts.txt', 'a', encoding='utf-8')
#
#
#
#
#
# def create_contact():
#     data = open('contacts.txt', 'a', encoding='utf-8')
#     add_contact = input('Введите данные контакта: ')
#     data.writelines('\n')
#     data.writelines(add_contact)
#     data.close()
#
# create_contact()
