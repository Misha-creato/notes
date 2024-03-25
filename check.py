import os


def is_note_number_exists(notes: list, note_number: int):
    note_number -= 1
    if note_number in range(len(notes)):
        return True
    return False


def is_file_exists_or_empty(file: str):
    if os.path.isfile(file) and os.path.getsize(file) > 0:
        return True
    return False


def is_load_json_valid(json_dict: dict):
    required_fields = ['title', 'text', 'created_at', 'updated_at']
    if all(field in json_dict for field in required_fields):
        return True
    return False
