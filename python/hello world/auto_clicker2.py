from pynput import keyboard
import time

repeat_times = 100
delay_between_press = .01
time_till_stop = 1
def on_press(key):
    print(key)
    if key == keyboard.Key.backspace:

        press_enter(repeat_times, delay_between_press, time_till_stop)



def press_enter(num_presses, delay, duration):

    start_time = time.time()

    end_time = start_time + duration



    while time.time() < end_time:

        for _ in range(num_presses):

            keyboard.Controller().press(keyboard.Key.enter)

            time.sleep(delay)

            keyboard.Controller().release(keyboard.Key.enter)



# Create a listener

listener = keyboard.Listener(on_press=on_press)

# Start the listener

listener.start()

# Wait for the listener to stop (e.g., by pressing Ctrl+C)

listener.join()
