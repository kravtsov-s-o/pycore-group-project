from data_managers.DataManager import DataManager
from decorators.HandleDecorator import HandleDecorator
from helpers.Pagination import Paginator
from NotesList import NotesList
from ui.UIManager import UIManager


class NotesListManager(DataManager):
    MENU_NOTES_LIST = {
        "title": "notes_list Menu",
        "items": [
            "1. Find",
            "2. Add",
            "3. Edit",
            "4. Delete",
            "5. Show All",
            "6. Exit",
        ],
    }
    MENU_EDIT_NOTE = {
        "title": "Edit Note Menu",
        "items": ["1. Edit all", "2. Title", "3. Content", "4. Tags", "5. Exit"],
    }

    def __init__(
        self, notes_list: NotesList, ui_manager: UIManager, items_per_page: int = 10
    ):
        self.notes_list = notes_list
        self.ui_manager = ui_manager
        self.items_per_page = items_per_page

    @HandleDecorator.handle_exception
    def find_items(self):
        self.ui_manager.clear_console()
        command = self.ui_manager.get_user_input("Find note(s)")
        if command.startswith("#"):
            notes = self.notes_list.find_sort(command)
        else:
            notes = self.notes_list.find_notes(command)

        if notes:
            items = Paginator(notes, self.items_per_page)
            self.ui_manager.show_items(items)
        else:
            self.ui_manager.show_message("List is empty...")

        self.ui_manager.wait_to_continue()

    @HandleDecorator.handle_exception
    def find_item(self):
        self.ui_manager.clear_console()
        choose_note = self.ui_manager.get_user_input("Search note for editing (Title)")
        current_record = self.notes_list.find_note(choose_note)
        if not choose_note:
            self.ui_manager.show_message(f"Note '{choose_note}' isn't found")
            self.ui_manager.wait_to_continue()
            return False

        self.ui_manager.show_message()
        self.ui_manager.show_message(choose_note)
        self.ui_manager.show_message()

        return current_record

    @HandleDecorator.handle_exception
    def add(self):
        self.ui_manager.clear_console()
        self.ui_manager.show_message("Example: title;content;#tag1,#tag2")
        command = self.ui_manager.get_user_input("Enter info")
        result = self.notes_list.add(command)

        if result:
            self.ui_manager.show_message("Note successfully saved")

        self.ui_manager.wait_to_continue()

    @HandleDecorator.handle_exception
    def edit(self):
        while True:
            current_note = self.notes_list

            if not current_note:
                return False

            self.ui_manager.show_menu(self.MENU_EDIT_NOTE)

            choice = self.ui_manager.get_user_input("Choose item")

            if choice == "1":
                self.ui_manaager.clear_console()
                self.ui_manager.show_message("Edit whole Note")
                self.ui_manager.show_message("Example: title;content;#tag1,#tag2")
                command = self.ui_manager.get_user_input("Enter info")
                result = self.notes_list.edit_note(current_note, command)
                if result:
                    self.ui_manager.show_message("Note updated successfully")
                    self.ui_manager.wait_to_continue()
                    break
            elif choice == "2":
                self.ui_manaager.clear_console()
                command = self.ui_manager.get_user_input("Enter Title")
                result = self.notes_list.edit_note(current_note, command, "title")
                if result:
                    self.ui_manager.show_message("Note updated successfully")
                    self.ui_manager.wait_to_continue()
                    break
            elif choice == "3":
                self.ui_manaager.clear_console()
                command = self.ui_manager.get_user_input("Enter content")
                result = self.notes_list.edit_note(current_note, command, "content")
                if result:
                    self.ui_manager.show_message("Note updated successfully")
                    self.ui_manager.wait_to_continue()
                    break
            elif choice == "4":
                self.ui_manaager.clear_console()
                command = self.ui_manager.get_user_input("Enter tags")
                result = self.notes_list.edit_note(current_note, command, "tags")
                if result:
                    self.ui_manager.show_message("Note updated successfully")
                    self.ui_manager.wait_to_continue()
                    break
            elif choice == "5":
                self.ui_manaager.clear_console()
                break
            else:
                self.ui_manaager.clear_console()
                self.ui_manager.show_message("Invalid choice. try again.")

    @HandleDecorator.handle_exception
    def delete(self):
        self.ui_manaager.clear_console()
        command = self.ui_manaager.get_user_input("Write Title")
        result = self.notes_list.delete(command)

        if result:
            self.ui_manager.show_message("Note successfully deleted")
        else:
            self.ui_manager.show_message("Note isn't found")

        self.ui_manaager.wait_to_continue()

    @HandleDecorator.handle_exception
    def show_all(self):
        self.ui_manager.clear_console()

        if len(self.notes_list.notes_list) > 0:
            items = Paginator(self.notes_list.notes_list, self.items_per_page)
            self.ui_manager.show_items(items)
        else:
            self.ui_manager.show_message("List is empty...")

        self.ui_manager.wait_to_continue()

    def run(self):
        while True:
            self.ui_manager.clear_console()
            self.ui_manager.show_menu(self.MENU_NOTES_LIST)
            choice = self.ui_manager.get_user_input("Choose item")

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
                break
            else:
                self.ui_manager.show_message("Invalid choice. try again.")
