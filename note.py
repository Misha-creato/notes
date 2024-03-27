from datetime import datetime
import json
import check
import interface


class Note:

    __title: str
    __text: str
    __created_at: datetime = datetime.now()
    __updated_at: datetime | None = None

    def get_title(self):
        return self.__title

    def set_title(self, new_title: str):
        self.__title = new_title

    def get_text(self):
        return self.__text

    def set_text(self, new_text: str):
        self.__text = new_text

    def get_created_at(self):
        if isinstance(self.__created_at, datetime):
            return self.__created_at.strftime('%d.%m.%Y %-I:%-M %p')
        return self.__created_at

    def set_created_at(self, created_at: datetime):  # устанавливается значение из json файла
        self.__created_at = created_at

    def get_updated_at(self):
        if self.__updated_at is None:
            return '--.--.---- --:-- --'
        if isinstance(self.__updated_at, datetime):
            return self.__updated_at.strftime('%d.%m.%Y %-I:%-M %p')
        return self.__updated_at

    def set_updated_at(self, update_at: datetime):
        self.__updated_at = update_at


class NoteEncoder(json.JSONEncoder):
    def default(self, obj):

        if isinstance(obj, Note):
            return {
                'title': obj.get_title(),
                'text': obj.get_text(),
                'created_at': obj.get_created_at(),
                'updated_at': obj.get_updated_at()
            }

        return json.JSONEncoder.default(self, obj)


def note_decoder(json_dict: dict):
    if check.is_load_json_valid(json_dict=json_dict):
        note = Note()
        note.set_title(json_dict['title'])
        note.set_text(json_dict['text'])
        note.set_created_at(json_dict['created_at'])
        note.set_updated_at(json_dict['updated_at'])
        return note
    interface.print_note_decoder(json_dict=json_dict)
    return None


class NoteManager:

    notes: list[Note]
    notes_file: str = '.notes.json'

    def get_note(self, note_number: int):
        note_number -= 1
        return self.notes[note_number]

    def edit_note(self, note_number: int):
        note = self.get_note(
            note_number=note_number
        )
        new_title, new_text = interface.get_edited_note(
            old_title=note.get_title(),
            old_text=note.get_text()
        )
        if new_title is not None:
            note.set_title(new_title)
        if new_text is not None:
            note.set_text(new_text)
        note.set_updated_at(datetime.now())

    def delete_note(self, note_number: int):
        note = self.get_note(note_number=note_number)
        self.notes.remove(note)
        interface.print_delete_note_message(title=note.get_title())

    def list_notes(self):
        interface.print_all_notes(notes=self.notes)

    def show_note(self, note_number: int):
        note = self.get_note(note_number=note_number)
        interface.print_note(
            title=note.get_title(),
            text=note.get_text(),
            created_at=note.get_created_at(),
            updated_at=note.get_updated_at()
        )

    def load_notes(self):
        if not check.is_file_exists_or_empty(file=self.notes_file):
            self.notes = []
        else:
            with open(self.notes_file, 'r') as file:
                self.notes = json.load(file, object_hook=note_decoder)
                self.notes = list(filter(lambda item: isinstance(item, Note), self.notes))

    def create_note(self, title: str, text: str):
        note = Note()
        note.set_title(new_title=title)
        note.set_text(new_text=text)
        self.notes.append(note)
        interface.print_create_note_message(title=note.get_title())

    def save_notes(self):
        with open(self.notes_file, 'w+') as file:
            json.dump(self.notes, file, indent=2, cls=NoteEncoder)
