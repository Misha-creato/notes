from datetime import datetime
import json
from prompt_toolkit import prompt
from key_bindings import bindings
import check


class Note:

    __title: str
    __text: str
    __created_at: datetime = datetime.now()
    __updated_at: datetime | str = 'Not updated yet'

    def get_title(self):
        return self.__title

    def set_title(self, new_title: str):
        self.__title = new_title

    def get_text(self):
        return self.__text

    def set_text(self, new_text: str):
        self.__text = new_text

    def get_created_at(self):
        return self.__created_at

    def set_created_at(self, created_at: datetime): # устанавливается значение из json файла
        self.__created_at = created_at

    def get_updated_at(self):
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

        if isinstance(obj, datetime):
            return obj.strftime('%d-%m-%Y %-I:%-M %p')
        return json.JSONEncoder.default(self, obj)


def note_decoder(json_dict: dict):
    if check.is_load_json_valid(json_dict=json_dict):
        note = Note()
        note.set_title(json_dict['title'])
        note.set_text(json_dict['text'])
        note.set_created_at(json_dict['created_at'])
        note.set_updated_at(json_dict['updated_at'])
        return note
    print('Note is invalid. Cannot load note.')
    return None


class NoteManager:

    notes: list[Note]
    notes_file: str = 'notes.json'

    def get_note(self, note_number: int):
        note_number -= 1
        return self.notes[note_number]

    def edit_note(self, note_number: int):
        note = self.get_note(note_number=note_number)
        new_title = prompt(
            message='Edit title (press Ctrl+A to exit): ',
            default=note.get_title(),
            key_bindings=bindings
        )
        if new_title is not None:
            note.set_title(new_title)
        new_text = prompt(
            message='Edit text (press Ctrl+D to complete entry or Ctrl+A to exit): \n',
            default=note.get_text(),
            multiline=True,
            key_bindings=bindings
        )
        if new_text is not None:
            note.set_text(new_text)
        note.set_updated_at(datetime.now())
        print(f'Note "{note.get_title()}" changed')

    def delete_note(self, note_number: int):
        note = self.get_note(note_number=note_number)
        self.notes.remove(note)
        print(f'Note "{note.get_title()}" successfully deleted')

    def show_notes(self):
        if self.notes:
            counter = 1
            for note in self.notes:
                print(f'{counter}) {note.get_title()} {note.get_created_at()}')
                counter += 1
        else:
            print('No notes')

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
        print(f'Created note "{note.get_title()}"')

    def save_notes(self):
        with open(self.notes_file, 'w+') as file:
            json.dump(self.notes, file, indent=2, cls=NoteEncoder)
