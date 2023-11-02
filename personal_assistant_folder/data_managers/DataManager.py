from abc import ABC, abstractmethod


class DataManager(ABC):
    @abstractmethod
    def find_items(self):
        pass

    @abstractmethod
    def find_item(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def show_all(self):
        pass

    @abstractmethod
    def run(self):
        pass
