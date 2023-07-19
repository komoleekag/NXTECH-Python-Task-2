import pyautogui
myscreen = pyautogui.screenshot()
myscreen.save('myscreen.png')
from PIL import ImageGrab
myscreen = ImageGrab.grab()
myscreen.save('myscreen_PIL.png')
from mss import mss
mss().shot()
for i in range(1,3):
    mss().shot(mon=i)
