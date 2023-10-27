import os
from functools import wraps
from personal_assistant_folder.sorting_files.Sorting import Sorting
from personal_assistant_folder.helpers.Pagination import Paginator
from personal_assistant_folder.AddressBook import AddressBook
from personal_assistant_folder.NotesList import NotesList

EMPTY_MESSAGE = 'List is empty ...'

menu_main = {
    'title': "Menu",
    'items': [
        "1. AddressBook",
        "2. Notes",
        "3. Sorting Files",
        "4. Exit"
    ]
}
menu_addressbook = {
    'title': "AddressBook Menu",
    'items': [
        "1. Find",
        "2. Add",
        "3. Edit",
        "4. Delete",
        "5. Show All",
        "6. Find contacts with birthdays",
        "7. Exit"
    ]
}
menu_single_contact = {
    'title': "Edit Contact Menu",
    'items': [
        "1. Edit all",
        "2. Name",
        "3. Phone",
        "4. Email",
        "5. Address",
        "6. Birthday",
        "7. Exit"
    ]
}
menu_notes_list = {
    'title': "notes_list Menu",
    'items': [
        "1. Find",
        "2. Add",
        "3. Edit",
        "4. Delete",
        "5. Show All",
        "6. Exit"
    ]
}
menu_single_note = {
    'title': "Edit Note Menu",
    'items': [
        "1. Edit all",
        "2. Title",
        "3. Content",
        "4. Tags",
        "5. Exit"
    ]
}


def clear_console() -> None:
    """
    Clear console
    """
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # MacOS и Linux
        os.system('clear')


def wait_to_continue() -> None:
    """
    Press 'Enter' to continue...
    """
    print()
    input('Press enter to continue...')


def get_divider(length: int, symbol: str = '-') -> str:
    """
    Get decorative string
    
    length: string length
    symbol: divider type - *, -, _
    """
    return symbol * length


def print_menu_list(menu: dict[str]) -> None:
    """
    Show menu title and items
    """
    max_length = len(menu['title'])

    for item in menu['items']:
        if len(item) > max_length:
            max_length = len(item)

    print(get_divider(max_length))
    print(menu['title'].center(max_length))
    print(get_divider(max_length))

    for item in menu['items']:
        print(item)

    print(get_divider(max_length))
    print()


def items_paginator(paginator: Paginator):
    """
    Show contacts and notes items by pages
    """
    while True:
        message = f'Page {paginator.current_page} from {paginator.total_pages} pages'
        str_length = len(message)
        clear_console()
        current_page = next(paginator)
        print(message)
        print()
        print(get_divider(str_length))
        for item in current_page:
            print(item)
            print(get_divider(str_length))
        print()
        print(message)
        print()

        action = input("Enter 'p' - prev page, 'n' - next page, 'q' - for exit: ").lower()

        if action == 'q':
            break

        paginator.move(action)


# ==================================================================================
# Functions helpers AddressBook
# ==================================================================================

def input_contact_info(prompt: str = "Enter info") -> str:
    """
    User`s commands
    """
    return input(f"{prompt}: ")


def handle_exception(func):
    """
    Декоратор для обработки исключений в функциях, выполняющих ввод.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ValueError as e:
            print(e)

    return wrapper


@handle_exception
def find_and_show_contacts(addressbook, items_per_page):
    """
    Find contacts for part of line
    """
    clear_console()
    command = input_contact_info()
    contacts = addressbook.find_records(command)
    if contacts:
        notes_paginator = Paginator(contacts, items_per_page)
        items_paginator(notes_paginator)
    else:
        print('List is empty ...')


@handle_exception
def add_contact(addressbook):
    """
    Add new contact
    """
    clear_console()
    print('Example: name;phone;birthday;email;address')
    command = input_contact_info()
    result = addressbook.add_record(command)
    if result:
        print('Contact successfully saved')
    wait_to_continue()


@handle_exception
def edit_contact(addressbook, current_record, choice3):
    """
    Edit contact
    """
    clear_console()
    if choice3 == "1":
        clear_console()
        print('Edit whole Contact')
        print('Example: name;phone;birthday;email;address')
        command = input_contact_info()
        result = addressbook.edit_record(current_record, command)
    elif choice3 == "2":
        clear_console()
        print('Edit Name')
        command = input_contact_info("Enter Name")
        result = addressbook.edit_record(current_record, command, 'name')
    elif choice3 == "3":
        clear_console()
        print('Edit Phone')
        command = input_contact_info("Enter phone")
        result = addressbook.edit_record(current_record, command, 'phone')
    elif choice3 == "4":
        clear_console()
        print('Edit Email')
        command = input_contact_info("Enter email")
        result = addressbook.edit_record(current_record, command, 'email')
    elif choice3 == "5":
        clear_console()
        print('Edit Address')
        command = input_contact_info("Enter address")
        result = addressbook.edit_record(current_record, command, 'address')
    elif choice3 == "6":
        clear_console()
        print('Edit Birthday')
        command = input_contact_info("Enter birthday date (dd.mm.yyyy)")
        result = addressbook.edit_record(current_record, command, 'birthday')
    elif choice3 == "7":
        return False  # Возвращаем False, чтобы указать, что нужно выйти из цикла
    else:
        print("Invalid choice. try again.")
        return True  # Возвращаем True, чтобы указать, что нужно продолжить цикл

    if result:
        print('Record updated successfully')
        wait_to_continue()

    return True


@handle_exception
def delete_contact(addressbook):
    """
    Delete contact
    """
    clear_console()
    try:
        command = input_contact_info("Delete (contact name)")
        result = addressbook.delete_record(command)
        if result:
            print('Contact successfully deleted')
        else:
            print("Contact isn't found")
    except ValueError as e:
        print(e)
    wait_to_continue()


def show_all_contacts(addressbook, items_per_page):
    """
    Show all contacts
    """
    clear_console()
    if len(addressbook.records) > 0:
        records_by_pages = Paginator(addressbook.records, items_per_page)
        items_paginator(records_by_pages)
    else:
        print(EMPTY_MESSAGE)
    wait_to_continue()


@handle_exception
def show_upcoming_birthday_contacts(addressbook, items_per_page):
    clear_console()
    command = input_contact_info("Enter count days")
    contacts = addressbook.get_upcoming_birthday_contacts(command)
    if len(contacts) > 0:
        records_by_pages = Paginator(contacts, items_per_page)
        items_paginator(records_by_pages)
    else:
        print(EMPTY_MESSAGE)
    wait_to_continue()


# ==================================================================================
# Functions helpers AddressBook - End
# ==================================================================================


def submenu_addressbook(addressbook, items_per_page):
    """
    Submenu for AddressBook
    """
    while True:
        # SubMenu AddressBook
        clear_console()
        print_menu_list(menu_addressbook)

        choice2 = input("Choose an item: ")
        # Find Contact
        if choice2 == "1":
            find_and_show_contacts(addressbook, items_per_page)

        # Add contact
        elif choice2 == "2":
            add_contact(addressbook)

        # Edit contact
        elif choice2 == "3":
            while True:
                clear_console()
                choose_record = input_contact_info('Search contact for editing (Name)')
                current_record = addressbook.find_record(choose_record)
                if not current_record:
                    print(f"Contact '{choose_record}' isn't found")
                    wait_to_continue()
                    break

                print()
                print(current_record)
                print()

                print_menu_list(menu_single_contact)

                choice3 = input_contact_info('Choose an item')
                if not edit_contact(addressbook, current_record, choice3):
                    break  # Если edit_contact возвращает False, выходим из цикла

        # Delete contact
        elif choice2 == "4":
            delete_contact(addressbook)

        # Show all
        elif choice2 == "5":
            show_all_contacts(addressbook, items_per_page)

        elif choice2 == "6":
            show_upcoming_birthday_contacts(addressbook, items_per_page)

        elif choice2 == "7":
            clear_console()
            break
        else:
            clear_console()
            print("Invalid choice. try again.")


# ==================================================================================
# Functions helpers Notes
# ==================================================================================
@handle_exception
def search_notes(notes_list, items_per_page):
    clear_console()
    command = input_contact_info("Find note(s)")
    if command.startswith('#'):
        notes = notes_list.find_sort(command)
    else:
        notes = notes_list.find_notes(command)

    if notes:
        notes_paginator = Paginator(notes, items_per_page)
        items_paginator(notes_paginator)
    else:
        print(EMPTY_MESSAGE)
    wait_to_continue()


@handle_exception
def add_note(notes_list):
    clear_console()
    print('Example: title;content;#tag1,#tag2')
    command = input_contact_info("Enter info")
    result = notes_list.add(command)
    if result:
        print('Note successfully saved')
    wait_to_continue()


@handle_exception
def edit_note(notes_list, current_note):
    while True:
        clear_console()
        print(current_note)
        print_menu_list(menu_single_note)
        choice3 = input_contact_info("Choose an item")

        if choice3 == "1":
            clear_console()
            print('Edit whole Note')
            print('Example: title;content;#tag1,#tag2')
            command = input_contact_info("Enter info")
            result = notes_list.edit_note(current_note, command)
            if result:
                print('Note updated successfully')
                wait_to_continue()
                break
        elif choice3 == "2":
            clear_console()
            command = input_contact_info("Enter Title")
            result = notes_list.edit_note(current_note, command, 'title')
            if result:
                print('Note updated successfully')
                wait_to_continue()
                break
        elif choice3 == "3":
            clear_console()
            command = input_contact_info("Enter content")
            result = notes_list.edit_note(current_note, command, 'content')
            if result:
                print('Note updated successfully')
                wait_to_continue()
                break
        elif choice3 == "4":
            clear_console()
            command = input_contact_info("Enter tags")
            result = notes_list.edit_note(current_note, command, 'tags')
            if result:
                print('Note updated successfully')
                wait_to_continue()
                break
        elif choice3 == "5":
            clear_console()
            break
        else:
            clear_console()
            print("Invalid choice. try again.")


@handle_exception
def delete_note(notes_list):
    clear_console()
    command = input_contact_info("Write Title")
    result = notes_list.delete(command)
    if result:
        print('Note successfully deleted')
    else:
        print("Note isn't found")
    wait_to_continue()


@handle_exception
def show_all_notes(notes_list, items_per_page):
    clear_console()
    if len(notes_list.notes_list) > 0:
        notes_paginator = Paginator(notes_list.notes_list, items_per_page)
        items_paginator(notes_paginator)
    else:
        print(EMPTY_MESSAGE)
    wait_to_continue()


# ==================================================================================
# Functions helpers Notes
# ==================================================================================

def submenu_notes(notes_list, items_per_page):
    while True:
        clear_console()
        print_menu_list(menu_notes_list)
        choice2 = input_contact_info("Choice item")

        if choice2 == "1":
            search_notes(notes_list, items_per_page)
        elif choice2 == "2":
            add_note(notes_list)
        elif choice2 == "3":
            choose_note = input_contact_info("Search note for editing (Title)")
            current_note = notes_list.find_note(choose_note)
            if not current_note:
                print(f"Note '{choose_note}' isn't found")
                wait_to_continue()
            else:
                edit_note(notes_list, current_note)
        elif choice2 == "4":
            delete_note(notes_list)
        elif choice2 == "5":
            show_all_notes(notes_list, items_per_page)
        elif choice2 == "6":
            clear_console()
            break
        else:
            clear_console()
            print("Invalid choice. try again.")


def submenu_sorting():
    """
    SubMenu for Sorting files in folder
    """
    while True:
        clear_console()

        print("--------------------")
        print("Sort files in folder")
        print("--------------------")
        print()

        choice2 = input_contact_info("Folder path (or 'exit / q')")

        if choice2.lower() in ["exit", 'q']:
            clear_console()
            break
        else:
            clear_console()

            try:
                sorting = Sorting(choice2)
                sorting.sort()
            except ValueError as e:
                print(e)

            print('Finish')
            wait_to_continue()
            break


def show_menu(addressbook: AddressBook, notes_list: NotesList, items_per_page: int) -> None:
    while True:
        clear_console()
        print_menu_list(menu_main)

        choice1 = input_contact_info("Where are you want to start")
        # AddressBook Menu
        if choice1 == "1":
            submenu_addressbook(addressbook, items_per_page)

        # SubMenu Notes
        elif choice1 == "2":
            submenu_notes(notes_list, items_per_page)

        # SubMenu Sorting Files
        elif choice1 == "3":
            submenu_sorting()

        # Close App
        elif choice1 == "4":
            clear_console()
            print('See you later!')
            break
        # Invalid command
        else:
            clear_console()
            print("Invalid choice. try again.")
           