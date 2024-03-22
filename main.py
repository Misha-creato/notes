import argparse
import json
import datetime
from prompt_toolkit import prompt
from prompt_toolkit.key_binding import KeyBindings
from note import Note
from note_json import (
    NoteEncoder,
    NoteDecoder
)


save_file = 'notes.json'



def get_arguments():
    parser = argparse.ArgumentParser(description='Notes')
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-c',
        # '--create',
        nargs='+',
        metavar=('header', 'text'),
        help='create a new note'
    )
    group.add_argument(
        '-s',
        # '--show',
        action='store_true',
        help='show list of notes'
    )
    group.add_argument(
        '-e',
        # '--edit',
        nargs=1,
        type=int,
        metavar='note number',
        help='edit a note'
    )
    group.add_argument(
        '-d',
        # '--delete',
        nargs=1,
        type=int,
        metavar='note number',
        help='delete a note'
    )

    # parser.add_argument(
    #     '-h',
    #     type=str,
    #     help='help'
    # )
    args = parser.parse_args()

    return args


def main():
    args = get_arguments()
    if args.c:
        if len(args.c) == 1:
            text = prompt(
                message='Input text (press Ctrl+D to complete entry): \n',
                multiline=True,
                key_bindings=bindings
            )

            args.c.append(text)
        print(args.c)
        n = Note()
        n.set_header(args.c[0])
        n.set_text(args.c[1])

        with open(save_file, 'a') as file:
            json.dump(n, file, indent=2, cls=NoteEncoder)

    elif args.s:
        notes = get_notes()
        counter = 1
        for note in notes:
            print(f'{counter}) {note.get_header()} {note.get_created_at()}')
            counter += 1

    elif args.e:
        edit_note(note_number=args.e[0])

    elif args.d:
        notes = get_notes()
        note = args.d[0]
        notes.remove(note)

    else:
        pass


def edit_note(note_number: int):
    notes = get_notes()
    note = notes[note_number - 1]
    new_header = prompt(
        message='Edit header: ',
        default=note.get_header()
    )
    note.set_header(new_header)
    new_text = prompt(
        message='Edit text (press Ctrl+D to complete entry): \n',
        default=note.get_text(),
        multiline=True,
        key_bindings=bindings
    )
    note.set_text(new_text)
    print(note.get_text())
    note.set_updated_at(datetime.datetime.now())


bindings = KeyBindings()

@bindings.add('c-d')
def _(event):
    event.app.exit(result=event.cli.current_buffer.text)


def get_notes():
    with open(save_file, 'r') as file:
        notes = json.load(file, cls=NoteDecoder)
        return notes


if __name__ == '__main__':
    main()

