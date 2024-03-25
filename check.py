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
