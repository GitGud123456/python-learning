
from pynput import keyboard
import time
import random
str = "text test time hey"
array = list(str)


def press_key(array):
    for letter in array:
        keyboard.Controller().press(letter)
        time.sleep(get_rand_delay())


def get_rand_delay():
    delay = random.randrange(20,40)
    delay = delay/100
    return delay


def start(start_key):
    if start_key == keyboard.Key.esc:
        press_key(array)


# Create a listener

listener = keyboard.Listener(on_press=start)

# Start the listener

listener.start()

# Wait for the listener to stop (e.g., by pressing Ctrl+C)

listener.join()
