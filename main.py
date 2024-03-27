from note import NoteManager
from arguments import get_arguments
from check import is_note_number_exists
import interface


def work_with_note(note_manager: NoteManager, note_number: int, action_key: str):
    actions = {
        'edit': note_manager.edit_note,
        'delete': note_manager.delete_note,
        'show': note_manager.show_note
    }
    action = actions[action_key]
    if is_note_number_exists(note_number=note_number, notes=note_manager.notes):
        action(note_number=note_number)
    else:
        interface.print_note_number_error(note_number=note_number)


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

    elif args.list:
        note_manager.list_notes()

    elif args.edit:
        note_number = args.edit[0]
        work_with_note(
            note_manager=note_manager,
            note_number=note_number,
            action_key='edit'
        )

    elif args.delete:
        note_number = args.delete[0]
        work_with_note(
            note_manager=note_manager,
            note_number=note_number,
            action_key='delete'
        )

    elif args.show:
        note_number = args.show[0]
        work_with_note(
            note_manager=note_manager,
            note_number=note_number,
            action_key='show'
        )

    note_manager.save_notes()


if __name__ == '__main__':
    main()
