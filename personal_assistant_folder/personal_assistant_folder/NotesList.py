from personal_assistant_folder.notes.Note import Note
from personal_assistant_folder.helpers.Serialization import Serialization


class NotesList:
    def __init__(self, filename):
        self.filename = filename
        self.notes_list = Serialization.load_from_file(self.filename)

    def _unique_title(self, value):
        for note in self.notes_list:
            if str(note.title) == value:
                raise ValueError('This Title already exist!')

    def add(self, value):
        # !!!Attention!!!
        # value - string from 3 part separate ';'
        # tags in value separate ','
        # Example: Title;Content;#tag1,#tag2,#tag3

        try:
            title, content, tags = value.split(';')
            self._unique_title(title)  # Перевірка на унікальність title
            note = Note(title, content)

            if tags:
                tags_list = tags.split(',')
                for tag in tags_list:
                    note.add_tag(tag)

            self.notes_list.append(note)

            Serialization.save_to_file(self.notes_list, self.filename)

            return True

        except ValueError:
            raise ValueError("Invalid data format\nExample: Title;Content;#tag1,#tag2,#tag3")

    def edit_note(self, note, data, field=None):
        try:
            if field is None:  # редагування всих полів
                title, content, tags = data.split(';')
                note.edit_title(title)
                note.edit_content(content)

                note.tags.clear()
                if tags:
                    tags_list = tags.split(',')
                    for tag in tags_list:
                        note.add_tag(tag)
            # редагування відповідних полів
            elif field == 'title':
                note.edit_title(data)
            elif field == 'content':
                note.edit_title(data)
            elif field == 'tags':
                note.tags.clear()
                tags_list = data.split(',')
                for tag in tags_list:
                    note.add_tag(tag)
            else:
                raise ValueError("Invalid field name for editing")

            Serialization.save_to_file(self.notes_list, self.filename)

            return True

        except ValueError:
            raise ValueError("Invalid data for editing\nExample: title;content;#tag1,#tag2,#tag3, or single one")

    def find_note(self, value):
        for note in self.notes_list:
            if str(note.title) == value:
                return note

        return None

    def delete(self, value):
        # !!!Attention!!!
        # Find and delete Note work only by it title
        result = False
        for note in self.notes_list:
            if value == note.title._value:
                self.notes_list.remove(note)
                Serialization.save_to_file(self.notes_list, self.filename)
                result = True
        return result

    def find_notes(self, value):
        found_notes = []
        for note in self.notes_list:
            if value in note.title.value or value in note.content.value:
                found_notes.append(note)

        if not found_notes:
            found_notes.append('Nothing found!')

        return found_notes

    def find_sort(self, value: str):
        result_list = []
        title_to_note = {}

        for note in self.notes_list:
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
