'''import time
import pyautogui
import os
import glob
global folder_path,file_list

folder_path = 'F:\GitHub\python-learning\python\hello world\screenCapture\ScreenShots'
file_list = glob.glob(os.path.join(folder_path,'*'))


def takeScreenShot():
    ScreenShot = pyautogui.screenshot()
    ScreenShot.save(f'{folder_path}\ScreenShot{len(file_list)+1}.png')


def watch(delay,boolean):
    file_list = glob.glob(os.path.join(folder_path,'*'))
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
'''

import time
import pyautogui
import os

folder_path = 'F:\GitHub\python-learning\python\hello world\screenCapture\ScreenShots'



def takeScreenShot(file_list):
    screenshot = pyautogui.screenshot()
    screenshot.save(os.path.join(folder_path, f'ScreenShot{len(file_list)}.png'))


def watch(delay, boolean):

    while boolean:
        file_list = os.listdir(folder_path)
        if len(file_list) > 10:
            #file_list.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
            os.remove(os.path.join(folder_path, file_list[-1]))
            print("Removed oldest screenshot")

        else:
            takeScreenShot(file_list)
            print("Not removed")
        time.sleep(delay)

def deleteScreenshots(folder_path):
    file_list = os.listdir(folder_path)
    for file_name in file_list:
        if file_name.endswith('.png'):
            file_path = os.path.join(folder_path, file_name)
            os.remove(file_path)

    print("All screenshots have been deleted.")




watch(1, True)
#deleteScreenshots(folder_path)
