from personal_assistant_folder.application.Application import Application
from personal_assistant_folder.data_managers.DataManager import DataManager
from personal_assistant_folder.data_managers.FileSorter import FileSorter
from personal_assistant_folder.ui.UIManager import UIManager


class ConsoleApplication(Application):
    MAIN_MENU = {
        'title': "Menu",
        'items': [
            "1. AddressBook",
            "2. Notes",
            "3. Sorting Files",
            "4. Exit"
        ]
    }

    def __init__(self, ui_manager: UIManager, addressbook_manager: DataManager, notes_list_manager: DataManager,
                 file_sorter: FileSorter):
        self.ui_manager = ui_manager
        self.addressbook_manager = addressbook_manager
        self.notes_list_manager = notes_list_manager
        self.file_sorter = file_sorter

    def run(self):
        while True:
            self.ui_manager.clear_console()
            self.ui_manager.show_menu(self.MAIN_MENU)
            choice = self.ui_manager.get_user_input('Choose item')
            if choice == "1":
                self.addressbook_manager.run()
            elif choice == "2":
                self.notes_list_manager.run()
            elif choice == "3":
                self.file_sorter.run()
                continue
            elif choice == "4":
                self.ui_manager.clear_console()
                print("See you later!")
                break
            else:
                print("Invalid choice. Please try again.")
