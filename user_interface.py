from err_check import check_new_data
from db_work import *
from db_export import *


def menu():
    while True:
        read_all()
        print(f"Телефонный справочник\n{'=' * 21}")
        actions = input("1. Показать все\n"
                        "2. Найти\n"
                        "3. Добавить\n"
                        "4. Редактировать\n"
                        "5. Удалить\n"
                        "6. Импорт\Экспорт\n"
                        "7. Выход\n")
        match actions:
            case "1":
                print_all()
            case "2":
                find_entry(input("Введите фамилию или номер телефона: "), read_all())
            case "3":
                add_entry(add_menu())
            case "4":
                print_all()
                id_change = input(f"Введите id: ")
                if find_entry(id_change, read_all()) and (answer := edit_menu()):
                    edit_entry(answer, id_change)
            case "5":
                del_entry(input("Введите фамилию или номер телефона: "))
            case "6":
                import_export_menu()
            case "7":
                logging.info("Stop program.\n")
                print("Спасибо за внимание!")
                break
            case _:
                logging.warning(f"Main menu, wrong item selected.")
                print("Ничего не вышло, введите еще раз.")


def add_menu():
    logging.info('Start add menu')
    add_dict = {"id": "1", "name": "", "surname": "", "phone": "", "description": ""}
    for i in add_dict:
        if i != "id":
            add_dict[i] = check_new_data(i)
    logging.info('Stop edit menu')
    return add_dict


def edit_menu():
    add_dict = {"1": "name", "2": "surname", "3": "phone", "4": "description"}
    logging.info('Start edit menu')
    while True:
        print("\nChanging:")
        change = input("1. имя\n"
                       "2. фамилия\n"
                       "3. телефон\n"
                       "4. адрес эл. почты\n"
                       "5. выход\n")

        match change:
            case "1" | "2" | "3" | "4":
                type_date = add_dict[change]
                return type_date, check_new_data(type_date)
            case "5":
                logging.info('Exited the edit menu')
                return 0
            case _:
                logging.warning(f"Edit menu, wrong item selected.")
                print("Повторите ввод.")


def import_export_menu():
    logging.info('Start import/export menu')
    while True:
        print("\Импорт\\Экспорт:")
        change = input("1. Импорт\n"
                       "2. Экспорт\n"
                       "3. Выход\n")
        match change:
            case "1":
                file_import(input(f"Введите имя файла: "))
                return
            case "2":
                while True:
                    logging.info('Start choose a format menu')
                    format_type = input(f"Bыберете формат:\n"
                                        f"1. CSV\n"
                                        f"2. JSON\n"
                                        f"3. exit\n")
                    match format_type:
                        case "1":
                            save_csv(input("Введите имя файла: "))
                            return
                        case "2":
                            save_json(input("Введите имя файла: "))
                            return
                        case "3":
                            logging.info('Exited the choose a format menu')
                            return
                        case _:
                            logging.warning(f"Choose a format menu, wrong item selected.")
                            print("Повторите ввод.")

            case "3":
                logging.info('Exited the import/export menu')
                break
            case _:
                logging.warning(f"Import/export menu, wrong item selected.")
                print("Повторите ввод.")
