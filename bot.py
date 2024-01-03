import time
import pyautogui 
import keyboard
import random
import win32api
import win32con

def mouse_click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed("x") == False:
    if pyautogui.pixel(2764,530)[0] == 0:
        mouse_click(2764,530)
    if pyautogui.pixel(2835, 530)[0] == 0:
        mouse_click(2835, 530)
    if pyautogui.pixel(2911, 530)[0] == 0:
        mouse_click(2911, 530)
    if pyautogui.pixel(2974, 530)[0] == 0:
        mouse_click(2974, 530)
        