import view
from classes import Contact, PhoneBook
import text as txt

pb = PhoneBook('phone_book.txt')

def start_phone_book():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                pb.load()
                view.print_info(txt.load_successful)
            case 2:
                pb.save()
                view.print_info(txt.save_successful)
            case 3:
                pb1 = pb.get()
                view.show_contact(pb1, txt.error_phone_book)
            case 4:
                contact = view.new_contact()
                pb.add(contact)
                view.print_info(txt.info_new_contact)
            case 5:
                search_1 = view.search_contact()
                result = pb.find(search_1)
                view.show_contact(result, txt.info_search_contact)
            case 6:
                search_2 = view.search_contact()
                result_1 = pb.find(search_2)
                view.show_contact(result_1, txt.info_search_contact)
                if result_1:
                    view.print_info(txt.info_edit_contact)
                    new_name = view.new_contact()
                    pb.edit(result_1, new_name)
            case 7:
                search_3 = view.search_contact()
                result_2 = pb.find(search_3)
                view.show_contact(result_2, txt.info_search_contact)
                if result_2:
                    pb.delete(result_2)
                    view.print_info(txt.delete_contact)
            case 8:
                if pb.save_on_exit():
                    if view.confirm(txt.answer_save):
                        pb.save()
                exit()



