import time
import pyautogui
seconds = time.time()

local_time = time.ctime(seconds)

print("Local time:", local_time)



#if program running
def takeScreenShot():
    ScreenShot = pyautogui.screenshot()
    ScreenShot.save('f:\GitHub\python-learning\screenCapture\ScreenShots.data')

takeScreenShot()