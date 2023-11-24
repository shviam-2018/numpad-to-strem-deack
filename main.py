import pynput.keyboard as kb
from pynput.keyboard import Listener

def on_press(key):
    if key == kb.Key.num_1:
        print("Hello, World!")

with Listener(on_press=on_press) as listener:
    listener.join()
