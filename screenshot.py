import pyautogui
import time

def screenshot(delay, name):
    time.sleep(delay)
    screenshot = pyautogui.screenshot()
    screenshot.save(name)


