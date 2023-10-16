from Note import Note


class NotesList:
    def __init__(self):
        self.noteslist = list()

    # def _unique_title(self, value):
    #     for note in self.noteslist:
    #         if str(note.title) == value:
    #             raise ValueError('This Title already exist!')

    def add(self, value):
        # !!!Attention!!!
        # value - string from 3 part separate ';'
        # tags in value separate ','
        # Example: Title;Content;#tag1,#tag2,#tag3

        try:
            title, content, tags = value.split(';')

            note = Note(title, content)

            if tags:
                tags_list = tags.split(',')
                for tag in tags_list:
                    note.add_tag(tag)

            self.noteslist.append(note)

        except ValueError:
            raise ValueError("Invalid data format\nExample: Title;Content;#tag1,#tag2,#tag3")

    def edit_note(self, title, new_value):
        # Search for a note by title
        note_to_edit = next((note for note in self.noteslist if note.title == title), None)

        if not note_to_edit:
            # If a note with the specified title is not found, raise an exception
            raise ValueError(f"Note with title '{title}' not found")

        # Split the new value into title, content, and tags using the delimiter ";"
        try:
            new_title, new_content, new_tags = new_value.split(';')
        except ValueError:
            raise ValueError("Invalid data format for editing\nExample: Title;Content;#tag1,#tag2,#tag3")

        # Update the title and content of the note
        note_to_edit.title = new_title
        note_to_edit.content = new_content

        # Clear the list of note tags
        note_to_edit.tags.clear()

        # If there are new tags, split them by comma and add them to the note
        if new_tags:
            tags_list = new_tags.split(',')
            for tag in tags_list:
                note_to_edit.add_tag(tag)

    def delete(self, value):
        # !!!Attention!!!
        # Find and delete Note work only by it title
        try:
            for note in self.noteslist:
                if str(note.title) == value:
                    self.noteslist.remove(note)
        except ValueError:
            pass

    def find_note(self, value):
        found_notes = []
        for note in self.noteslist:
            if value in note.title.value or value in note.content.value:
                found_notes.append(note)
        return found_notes

    def find_sort(self, value: str):
        result_list = []
        title_to_note = {}

        for note in self.noteslist:
            for tag in note.tags:
                if value == tag.value:
                    title = note.title.value
                    if title not in title_to_note:
                        title_to_note[title] = note

        found_titles = list(title_to_note.keys())
        found_titles.sort()

        for title in found_titles:
            result_list.append(title_to_note[title])

        return result_list
