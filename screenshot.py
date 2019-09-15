import pyautogui
import time

def screenshot(delay):
    time.sleep(delay)
    screenshot = pyautogui.screenshot()
    screenshot.save("image/realtime_screenshot/screenshot.png")


