# Let's go

from pynput import keyboard

def register_keystrokes():
    def on_press(key):
        try:
            print('Key {0} pressed.'.format(key.char))
        except AttributeError:
            print('Special key {0} pressed.'.format(key))

    def on_release(key):
        print('Key {0} released.'.format(key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    # Collect events until released
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == '__main__':
    register_keystrokes()