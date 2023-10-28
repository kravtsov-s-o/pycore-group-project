from personal_assistant_folder.AddressBook import AddressBook
from personal_assistant_folder.NotesList import NotesList
from personal_assistant_folder.data_managers.AddressBookManager import AddressBookManager
from personal_assistant_folder.data_managers.NotesListManager import NotesListManager
from personal_assistant_folder.data_managers.FileSorter import FileSorter
from personal_assistant_folder.ui.ConsoleUIManager import ConsoleUIManager
from personal_assistant_folder.application.ConsoleApplication import ConsoleApplication

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
