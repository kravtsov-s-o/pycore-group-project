from AddressBook import AddressBook
from data_managers.DataManager import DataManager
from decorators.HandleDecorator import HandleDecorator
from helpers.Pagination import Paginator
from ui.UIManager import UIManager


class AddressBookManager(DataManager):
    MENU_ADDRESS_BOOK = {
        "title": "AddressBook Menu",
        "items": [
            "1. Find",
            "2. Add",
            "3. Edit",
            "4. Delete",
            "5. Show All",
            "6. Find contacts with birthdays",
            "7. Exit",
        ],
    }
    MENU_EDIT_CONTACT = {
        "title": "Edit Contact Menu",
        "items": [
            "1. Edit all",
            "2. Name",
            "3. Phone",
            "4. Email",
            "5. Address",
            "6. Birthday",
            "7. Exit",
        ],
    }

    def __init__(
        self, addressbook: AddressBook, ui_manager: UIManager, items_per_page: int = 10
    ):
        self.addressbook = addressbook
        self.ui_manager = ui_manager
        self.items_per_page = items_per_page

    @HandleDecorator.handle_exception
    def find_items(self):
        """
        Find contacts for part of line and show with pages of items
        """
        self.ui_manager.clear_console()

        command = self.ui_manager.get_user_input()

        contacts = self.addressbook.find_records(command)

        if contacts:
            notes_paginator = Paginator(contacts, self.items_per_page)
            self.ui_manager.show_items(notes_paginator)
        else:
            self.ui_manager.show_message("List is empty ...")

    @HandleDecorator.handle_exception
    def find_item(self):
        """
        Find item for edit
        """
        self.ui_manager.clear_console()
        choose_record = self.ui_manager.get_user_input(
            "Search contact for editing (Name)"
        )
        current_record = self.addressbook.find_record(choose_record)
        if not current_record:
            self.ui_manager.show_message(f"Contact '{choose_record}' isn't found")
            self.ui_manager.wait_to_continue()
            return False

        self.ui_manager.show_message()
        self.ui_manager.show_message(current_record)
        self.ui_manager.show_message()

        return current_record

    @HandleDecorator.handle_exception
    def add(self):
        """
        Add new contact
        """
        self.ui_manager.clear_console()
        self.ui_manager.show_message("Example: name;phone;birthday;email;address")
        command = self.ui_manager.get_user_input()
        result = self.addressbook.add_record(command)
        if result:
            self.ui_manager.show_message("Contact successfully saved")
        self.ui_manager.wait_to_continue()

    @HandleDecorator.handle_exception
    def edit(self):
        """
        Edit contact
        """
        current_record = self.find_item()

        if not current_record:
            return False

        self.ui_manager.show_menu(self.MENU_EDIT_CONTACT)

        choice = self.ui_manager.get_user_input("Choose item")

        self.ui_manager.clear_console()
        if choice == "1":
            self.ui_manager.clear_console()
            self.ui_manager.show_message("Edit whole Contact")
            self.ui_manager.show_message("Example: name;phone;birthday;email;address")
            command = self.ui_manager.get_user_input()
            result = self.addressbook.edit_record(current_record, command)
        elif choice == "2":
            self.ui_manager.clear_console()
            self.ui_manager.show_message("Edit Name")
            command = self.ui_manager.get_user_input("Enter Name")
            result = self.addressbook.edit_record(current_record, command, "name")
        elif choice == "3":
            self.ui_manager.clear_console()
            self.ui_manager.show_message("Edit Phone")
            command = self.ui_manager.get_user_input("Enter phone")
            result = self.addressbook.edit_record(current_record, command, "phone")
        elif choice == "4":
            self.ui_manager.clear_console()
            self.ui_manager.show_message("Edit Email")
            command = self.ui_manager.get_user_input("Enter email")
            result = self.addressbook.edit_record(current_record, command, "email")
        elif choice == "5":
            self.ui_manager.clear_console()
            self.ui_manager.show_message("Edit Address")
            command = self.ui_manager.get_user_input("Enter address")
            result = self.addressbook.edit_record(current_record, command, "address")
        elif choice == "6":
            self.ui_manager.clear_console()
            self.ui_manager.show_message("Edit Birthday")
            command = self.ui_manager.get_user_input("Enter birthday date (dd.mm.yyyy)")
            result = self.addressbook.edit_record(current_record, command, "birthday")
        elif choice == "7":
            return False  # Возвращаем False, чтобы указать, что нужно выйти из цикла
        else:
            self.ui_manager.show_message("Invalid choice. try again.")
            return True  # Возвращаем True, чтобы указать, что нужно продолжить цикл

        if result:
            self.ui_manager.show_message("Record updated successfully")
            self.ui_manager.wait_to_continue()

        return True

    @HandleDecorator.handle_exception
    def delete(self):
        """
        Delete contact
        """
        self.ui_manager.clear_console()

        command = self.ui_manager.get_user_input("Delete (contact name)")
        result = self.addressbook.delete_record(command)
        if result:
            self.ui_manager.show_message("Contact successfully deleted")
        else:
            self.ui_manager.show_message("Contact isn't found")

        self.ui_manager.wait_to_continue()

    @HandleDecorator.handle_exception
    def show_all(self):
        """
        Show all contacts
        """
        self.ui_manager.clear_console()

        if len(self.addressbook.records) > 0:
            items = Paginator(self.addressbook.records, self.items_per_page)
            self.ui_manager.show_items(items)
        else:
            self.ui_manager.show_message("List is empty...")
            self.ui_manager.wait_to_continue()

    @HandleDecorator.handle_exception
    def show_upcoming_birthday_contacts(self):
        self.ui_manager.clear_console()
        command = self.ui_manager.get_user_input("Enter count days")
        contacts = self.addressbook.get_upcoming_birthday_contacts(command)
        if len(contacts) > 0:
            items = Paginator(contacts, self.items_per_page)
            self.ui_manager.show_items(items)
        else:
            self.ui_manager.show_message("List is empty...")
            self.ui_manager.wait_to_continue()

    def run(self):
        while True:
            self.ui_manager.clear_console()
            self.ui_manager.show_menu(self.MENU_ADDRESS_BOOK)
            choice = self.ui_manager.get_user_input()

            if choice == "1":
                self.find_items()
            elif choice == "2":
                self.add()
            elif choice == "3":
                self.edit()
            elif choice == "4":
                self.delete()
            elif choice == "5":
                self.show_all()
            elif choice == "6":
                self.show_upcoming_birthday_contacts()
            elif choice == "7":
                break
            else:
                self.ui_manager.show_message("Invalid choice. try again.")
