from pynput.keyboard import Key, Controller, Listener
import time
import pythoncom
import pyWinhook
global key_to_press,repeat_times,delay_between_press,time_till_stop
keyboard = Controller()
key_to_press = 13
repeat_times = 500
delay_between_press = .01
time_till_stop = 100000

def check_if_Q(event):
    if event.Key == "Q":
        press_enter(repeat_times,delay_between_press,timer)


def press_enter(num_presses, delay, duration):
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        for _ in range(num_presses):
            keyboard.press('enter')
            keyboard.release('enter')
            time.sleep(delay)

def loop(key,times,delay,timer):
    print("hi")
    num = 0
    while num < times: 
        keyboard.press(13)
        keyboard.release(13)
        time.sleep(delay)
        num +=1
    time.sleep(timer)
    return True

#loop(key_to_press,repeat_times,delay_between_press,time_till_stop)

'''
def OnKeyboardEvent(event):
    print('MessageName:',event.MessageName)
    print('Message:',event.Message)
    print('Time:',event.Time)
    print('Window:',event.Window)
    print('WindowName:',event.WindowName)
    print('Ascii:', event.Ascii, chr(event.Ascii))
    print('Key:', event.Key)
    print('KeyID:', event.KeyID)
    print('ScanCode:', event.ScanCode)
    print('Extended:', event.Extended)
    print('Injected:', event.Injected)
    print('Alt', event.Alt)
    print('Transition', event.Transition)
    print('---')

# return True to pass the event to other handlers
    return True
'''
# create a hook manager
hm = pyWinhook.HookManager()

# watch for all mouse events
#hm.KeyDown = OnKeyboardEvent
hm.KeyDown = check_if_Q
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
