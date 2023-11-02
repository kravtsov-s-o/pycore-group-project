from AddressBook import AddressBook
from NotesList import NotesList
from data_managers.AddressBookManager import AddressBookManager
from data_managers.NotesListManager import NotesListManager
from data_managers.FileSorter import FileSorter
from ui.ConsoleUIManager import ConsoleUIManager
from application.ConsoleApplication import ConsoleApplication

# BASE CONSTANTS
FILE_CONTACTS = 'contacts.bin'
FILE_NOTES = 'notes.bin'
ITEMS_PER_PAGE = 10


def init():
    ui_manager = ConsoleUIManager()
    addressbook_manager = AddressBookManager(AddressBook(FILE_CONTACTS), ui_manager, ITEMS_PER_PAGE)
    notes_list_manager = NotesListManager(NotesList(FILE_NOTES), ui_manager, ITEMS_PER_PAGE)
    file_sorter = FileSorter(ui_manager)

    app = ConsoleApplication(ui_manager, addressbook_manager, notes_list_manager, file_sorter)
    app.run()


if __name__ == "__main__":
    init()
