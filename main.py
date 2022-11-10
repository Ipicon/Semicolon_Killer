import keyboard


def change_binding():
    global is_latin
    is_latin = not is_latin

    return False


def enter_question(event):
    global is_latin

    if event.event_type == keyboard.KEY_DOWN:
        if is_latin:
            keyboard.write(';')  # greek question mark - 894 ascii code

        elif not is_latin:
            keyboard.write(';')  # normal semicolon

    return False


if __name__ == '__main__':
    is_latin = True
    keyboard.add_hotkey('ctrl+shift+.', change_binding)
    keyboard.hook_key(';', enter_question, suppress=True)

    keyboard.wait()
