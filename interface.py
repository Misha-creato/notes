from prompt_toolkit import prompt
from rich.console import Console
from rich.table import Table
from rich import box
from key_bindings import bindings
from prompt_toolkit.styles import Style


def print_note_decoder(json_dict: dict):
    print(f'Note {json_dict} is invalid. Cannot load note.')


def get_edited_note(old_title: str, old_text: str):
    custom_style = Style.from_dict({
        'prompt': '#d70087',
        'btn': 'reverse',
        '': '#00aa00',
    })
    new_title = prompt(
        message=[
            ('class:""', 'Edit title (press '),
            ('class:btn', 'Ctrl+A'),
            ('class:""', ' to exit): ')
        ],
        default=old_title,
        style=custom_style,
        key_bindings=bindings,
    )
    new_text = prompt(
        message=[
            ('class:""', 'Edit text (press '),
            ('class:btn', 'Ctrl+D'),
            ('class:""', ' to complete entry or '),
            ('class:btn', 'Ctrl+A'),
            ('class:""', ' to exit): \n')
        ],
        default=old_text,
        multiline=True,
        style=custom_style,
        key_bindings=bindings
    )
    print(f'Note "{old_title}" changed')
    return new_title, new_text


def print_delete_note_message(title: str):
    print(f'Note "{title}" successfully deleted')


def print_create_note_message(title: str):
    print(f'Created note "{title}"')


def print_all_notes(notes: list):

    if notes:
        table = Table(title="All notes", box=box.SIMPLE_HEAD)

        table.add_column("No.", justify="center", style="cyan")
        table.add_column("Title", justify="left", style="cyan", no_wrap=True)
        table.add_column("Create time", style="magenta")
        table.add_column("Update time", justify="left", style="green")

        for note in notes:
            table.add_row(
                str(notes.index(note) + 1) + ')',
                note.get_title(),
                note.get_created_at(),
                note.get_updated_at()
            )

        console = Console()
        console.print(table)

    else:
        print('No notes')


def print_note_number_error(note_number: int):
    print(f'Note number {note_number} is invalid')


def print_note(title: str, text: str, created_at: str, updated_at: str):
    console = Console()
    table = Table(show_header=False, box=None)
    table.add_column(style="dim")

    data = [
        ("Title", title),
        ("Create time", created_at),
        ("Update time", updated_at),
        ("Text", text),
    ]

    for row in data:
        table.add_row(row[0], row[1])

    console.print(table)
