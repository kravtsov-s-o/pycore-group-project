from sorting_files.Sorting import Sorting
from ui.UIManager import UIManager


class FileSorter:
    SORT_MENU = {"title": "Sort files in folder", "items": []}

    def __init__(self, ui_manager: UIManager):
        self.ui_manager = ui_manager

    def run(self):
        """
        SubMenu for Sorting files in folder
        """
        while True:
            self.ui_manager.clear_console()

            self.ui_manager.show_menu(self.SORT_MENU)

            user_string = self.ui_manager.get_user_input(
                "Folder path (or 'exit / q')"
            ).strip()

            if user_string.lower() in ["exit", "q"] or not user_string:
                self.ui_manager.clear_console()
                break
            else:
                self.ui_manager.clear_console()

                try:
                    sorting = Sorting(user_string)
                    sorting.sort()
                except ValueError as e:
                    self.ui_manager.show_menu(e)

                self.ui_manager.show_menu("Finish")
                self.ui_manager.wait_to_continue()
                break
