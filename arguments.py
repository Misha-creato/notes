import argparse


def get_arguments():
    parser = argparse.ArgumentParser(description='Notes app')
    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        '-c',
        '--create',
        nargs='+',
        type=str,
        metavar=('note title', 'note text'),
        help='Create a new note'
    )
    group.add_argument(
        '-l',
        '--list',
        action='store_true',
        help='Show list of all notes'
    )
    group.add_argument(
        '-e',
        '--edit',
        nargs=1,
        type=int,
        metavar='note number',
        help='Edit a note'
    )
    group.add_argument(
        '-d',
        '--delete',
        nargs=1,
        type=int,
        metavar='note number',
        help='Delete a note'
    )
    group.add_argument(
        '-s',
        '--show',
        nargs=1,
        type=int,
        metavar='note number',
        help='Show a note'
    )

    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()

    return args
