import pyautogui
from time import sleep

#調整音量→避免進入休眠模式
def prevent_screen_lock():
    sleep(30)
    pyautogui.press('volumeup')
    sleep(1)
    pyautogui.press('volumedown')
    sleep(30)

while True:
    prevent_screen_lock()