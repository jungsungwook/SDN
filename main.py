# pip install pypiwin32
# pip install pyautogui
# pip install pygetwindow
# pip install pyMeow-1.21.8.zip
import win32gui
import pyautogui
import pygetwindow as gw
import pyMeow as pm
from ctypes import *

# mouseleftdown = 1
# mouseleftup = 2
# mouserightdown = 4
# mouserightup = 8
# mousewheeldown = 16
# mousewheelup = 32

dd_dll = windll.LoadLibrary("./DD94687.64.dll")
st = dd_dll.DD_btn(0)

def left_click_dd(x, y):
    dd_dll.DD_mov(x, y)
    dd_dll.DD_btn(1)
    dd_dll.DD_btn(2)
    
def screenshot(window_title="MapleStory"):
    if window_title:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            win32gui.SetForegroundWindow(hwnd)
            x, y, x1, y1 = win32gui.GetClientRect(hwnd)
            x, y = win32gui.ClientToScreen(hwnd, (x, y))
            x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
            im = pyautogui.screenshot(region=(x, y, x1, y1))
            return im
        else:
            print('# Window not found!')
    else:
        # time.sleep(0.2)
        im = pyautogui.screenshot()
        return im

def read_offsets(proc, base_address, offsets):
    basepoint = pm.read_int(proc, base_address)
    current_pointer = basepoint  
    for i in offsets[:-1]:
        current_pointer = pm.read_int(proc, current_pointer+i)

    return current_pointer + offsets[-1]

def getWindows():
    title = gw.getAllTitles()
    print(title)

if __name__ == '__main__':
    print("# start")
    while True:
        x, y = pyautogui.position()
        print(pm.pixel_at_mouse())
        # 마우스 포인터의 색깔이 검은색이면
        if(pm.pixel_at_mouse() == {'x': 0, 'y': 0, 'color': {'r': 40, 'g': 42, 'b': 54, 'a': 255}}):
            # 현재 포인터 가져오기
            left_click_dd(x, y)
            print("# click -->", x, y)