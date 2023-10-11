import time
import pyautogui
import os
import glob
global folder_path
folder_path = 'F:\GitHub\python-learning\python\hello world\screenCapture\ScreenShots'

file_list = glob.glob(os.path.join(folder_path,'*'))
def takeScreenShot():
    ScreenShot = pyautogui.screenshot()
    ScreenShot.save(f'{folder_path}\ScreenShot.png')


takeScreenShot()

def watch(delay,boolean):
    while boolean:
        takeScreenShot()
        if len(file_list) >= 100:
            file_list.sort(key=os.path.getmtime)
            os.remove(file_list[0])
            print("removed")
        else:
            print("not removed")
    time.sleep(delay)

watch(0,True)

