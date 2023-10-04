from pynput.keyboard import Key, Controller, Listener
import time
import pythoncom
import pyWinhook as pyHook

keyboard = Controller()
key_to_press = "Return"
repeat_times = 50
delay_between_press = .01
time_till_stop = 4

def loop(key,times,delay,timer):

    while num < times: 
        keyboard.press(key)
        keyboard.release(key)
        time.sleep(delay)
    time.sleep(timer)
    return True

#loop(key_to_press,repeat_times,delay_between_press,time_till_stop)


def OnKeyboardEvent(event):
    print('MessageName:',event.MessageName)
    print('Message:',event.Message)
    print('Time:',event.Time)
    print('Window:',event.Window)
    print('WindowName:',event.WindowName)
    print('Ascii:', event.Ascii, chr(event.Ascii))
    print('Key:', event.Key)
    print(type(event,event.Key))
    if event.Key == "Q":
        loop(key_to_press,repeat_times,delay_between_press,time_till_stop)
    print('KeyID:', event.KeyID)
    print('ScanCode:', event.ScanCode)
    print('Extended:', event.Extended)
    print('Injected:', event.Injected)
    print('Alt', event.Alt)
    print('Transition', event.Transition)
    print('---')

# return True to pass the event to other handlers
    return True

# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()

qqqqqaaaaqqq