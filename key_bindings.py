from prompt_toolkit.key_binding import KeyBindings


bindings = KeyBindings()


@bindings.add('c-d')
def save_and_exit(event):
    event.app.exit(result=event.cli.current_buffer.text)


@bindings.add('c-a')
def exit_without_save(event):
    event.app.exit(result=None)
