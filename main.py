from note import NoteManager
from arguments import get_arguments
from check import is_note_number_exists


def main():
    args = get_arguments()
    note_manager = NoteManager()
    note_manager.load_notes()

    if args.create:
        if len(args.create) > 2:
            print('Too many values were passed')
        else:
            text = args.create[1] if len(args.create) == 2 else ''
            note_manager.create_note(title=args.create[0], text=text)

    elif args.show:
        note_manager.show_notes()

    elif args.edit:
        note_number = args.edit[0]
        if is_note_number_exists(note_number=note_number, notes=note_manager.notes):
            note_manager.edit_note(note_number=note_number)
        else:
            print('Note number is invalid')

    elif args.delete:
        note_number = args.delete[0]
        if is_note_number_exists(note_number=note_number, notes=note_manager.notes):
            note_manager.delete_note(note_number=note_number)
        else:
            print('Note number is invalid')

    note_manager.save_notes()


if __name__ == '__main__':
    main()
