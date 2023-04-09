import view
import model
import text as txt

def start_phone_book():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.load_file()
                view.print_info(txt.load_successful)
            case 2:
                model.save_file()
                view.print_info(txt.save_successful)
            case 3:
                pb = model.get_phone_book()
                view.show_contact(pb, txt.error_phone_book)
            case 4:
                contact = view.new_contact()
                model.add_contact(contact)
                view.print_info(txt.info_new_contact)
            case 5:
                search_1 = view.search_contact()
                result = model.find_contact(search_1)
                view.show_contact_2(result, txt.info_search_contact)
            case 6:
                search_2 = view.search_contact()
                result_1 = model.find_contact(search_2)
                view.show_contact_2(result_1, txt.info_search_contact)
                if result_1:
                    view.print_info(txt.info_edit_contact)
                    new_name = view.new_contact()
                    model.edit_contact(result_1, new_name)
            case 7:
                search_3 = view.search_contact()
                result_2 = model.find_contact(search_3)
                view.show_contact_2(result_2, txt.info_search_contact)
                if result_2:
                    model.delete_contact(result_2)
                    view.print_info(txt.delete_contact)
            case 8:
                if model.exit_pb():
                    if view.confirm(txt.answer_save):
                        model.save_file()
                exit()



