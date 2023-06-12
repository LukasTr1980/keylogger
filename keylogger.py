import os
from pynput import keyboard

def register_keystrokes():
    strokes_file = open(os.path.join(os.getcwd(), "strokes"), "w")

    def on_press(key):
        try:
            strokes_file.write('Key {0} pressed.\n'.format(key.char))
        except AttributeError:
            strokes_file.write('Special key {0} pressed.\n'.format(key))
        strokes_file.flush()

    def on_release(key):
        strokes_file.write('Key {0} released.\n'.format(key))
        strokes_file.flush()
        if key == keyboard.Key.esc:
            # Stop listener
            strokes_file.close()
            return False

    # Collect events until released
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == '__main__':
    register_keystrokes()