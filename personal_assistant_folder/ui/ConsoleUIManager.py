import os
from ui.UIManager import UIManager
from helpers.Pagination import Paginator


class ConsoleUIManager(UIManager):
    def get_user_input(self, prompt: str = 'Enter info'):
        return input(f"{prompt}: ")

    def show_message(self, message: str = ''):
        print(message)

    def clear_console(self) -> None:
        """
        Clear console
        """
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # MacOS и Linux
            os.system('clear')

    def wait_to_continue(self) -> None:
        """
        Press 'Enter' to continue...
        """
        self.show_message()
        print('Press enter to continue...')

    def get_divider(self, length: int = 10, symbol: str = '-') -> str:
        """
        Get decorative string

        length: string length
        symbol: divider type - *, -, _
        """
        return symbol * length

    def show_menu(self, menu: dict[str]):
        """
        Show menu
        """
        max_length = len(menu['title'])

        if menu['items']:
            for item in menu['items']:
                if len(item) > max_length:
                    max_length = len(item)

        self.show_message(self.get_divider(max_length))
        self.show_message(menu['title'].center(max_length))
        self.show_message(self.get_divider(max_length))

        if (menu['items']):
            for item in menu['items']:
                self.show_message(item)

            self.show_message(self.get_divider(max_length))
        self.show_message()

    def show_items(self, paginator: Paginator):
        """
        Show contacts and notes items by pages
        """
        while True:
            message = f'Page {paginator.current_page} from {paginator.total_pages} pages'
            str_length = len(message)
            self.clear_console()
            current_page = next(paginator)
            self.show_message(message)
            self.show_message()
            self.show_message(self.get_divider(str_length))

            for item in current_page:
                self.show_message(item)
                self.show_message(self.get_divider(str_length))

            self.show_message()
            self.show_message(message)
            self.show_message()

            action = self.get_user_input("Enter 'p' - prev page, 'n' - next page, 'q' - for exit").lower()

            if action == 'q':
                break

            paginator.move(action)
