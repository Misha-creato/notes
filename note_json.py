import json
import datetime
from note import Note


class NoteEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Note):
            return {
                'header': obj.get_header(),
                'text': obj.get_text(),
                'created_at': obj.get_created_at(),
                'updated_at': obj.get_updated_at()
            }
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%d-%m-%Y %-I:%-M %p')
        return json.JSONEncoder.default(self, obj)


class NoteDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.dict_to_note, *args, **kwargs)

    def dict_to_note(self, dict):
        if 'header' in dict and 'text' in dict and 'created_at' in dict:
            note = Note()
            note.set_header(dict['header'])
            note.set_text(dict['text'])
            note.set_created_at(dict['created_at'])
            note.set_updated_at(dict['updated_at'])
            return note
        return dict
