from abc import ABC, abstractmethod


class UIManager(ABC):
    @abstractmethod
    def get_user_input(self, prompt):
        pass

    @abstractmethod
    def show_message(self, message):
        pass

    @abstractmethod
    def show_items(self, items_paginator):
        pass

    @abstractmethod
    def show_menu(self, menu: dict[str]):
        pass
