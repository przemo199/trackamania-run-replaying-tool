import time

import pyautogui
import win32api
import win32con
import win32gui
import win32process
from pynput.keyboard import Key

pyautogui.FAILSAFE = True

# the middle of one of the starting lights on 1920x1080 resolution
START_POINT_TMNF = {"X": 610, "Y": 690, "COLOR": [110, 220, 70]}

KEYS = ["w", "s", "a", "d", "r", "esc", "shift", "delete"]

DEFAULT_FILE = "input_logs.txt"


def get_pixel_colour(i_x, i_y):
    i_desktop_window_id = win32gui.GetDesktopWindow()
    i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
    long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
    i_colour = int(long_colour)
    win32gui.ReleaseDC(i_desktop_window_id, i_desktop_window_dc)
    return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)


def is_within_margin(rgb, margin):
    if (START_POINT_TMNF["COLOR"][0] + margin > rgb[0] > START_POINT_TMNF["COLOR"][0] - margin and
            START_POINT_TMNF["COLOR"][1] + margin > rgb[1] > START_POINT_TMNF["COLOR"][1] - margin and
            START_POINT_TMNF["COLOR"][2] + margin > rgb[2] > START_POINT_TMNF["COLOR"][2] - margin):
        return True
    else:
        return False


def wait_for_green_light():
    while not is_within_margin(get_pixel_colour(START_POINT_TMNF["X"], START_POINT_TMNF["Y"]), 20):
        time.sleep(0.002)


def key_to_string(key):
    try:
        return key.char.lower()
    except AttributeError:
        if key == Key.shift:
            return "shift"
        elif key == Key.esc:
            return "esc"
        elif key == Key.delete:
            return "delete"
        else:
            return "unknown"


def string_to_key(key):
    if key == "shift":
        return Key.shift
    elif key == "esc":
        return Key.esc
    elif key == "delete":
        return Key.delete
    else:
        if len(key) == 1:
            return key


def set_priority(pid=None, priority=1):
    """ Function from: https://code.activestate.com/recipes/496767/
        Set The Priority of a Windows Process.  Priority is a value between 0-5 where
        2 is normal priority.  Default sets the priority of the current
        python process but can take any valid process ID. """

    priority_classes = [win32process.IDLE_PRIORITY_CLASS,
                        win32process.BELOW_NORMAL_PRIORITY_CLASS,
                        win32process.NORMAL_PRIORITY_CLASS,
                        win32process.ABOVE_NORMAL_PRIORITY_CLASS,
                        win32process.HIGH_PRIORITY_CLASS,
                        win32process.REALTIME_PRIORITY_CLASS]

    if pid is None:
        pid = win32api.GetCurrentProcessId()
    handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, True, pid)
    win32process.SetPriorityClass(handle, priority_classes[priority])
