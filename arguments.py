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
        '-s',
        '--show',
        action='store_true',
        help='Show list of notes'
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

    args = parser.parse_args()

    return args
