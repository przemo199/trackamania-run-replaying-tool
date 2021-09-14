import time

import pyautogui
from pynput.keyboard import Key, Listener
from utils import DEFAULT_FILE, key_to_string, KEYS, wait_for_green_light

pyautogui.FAILSAFE = True

start = time.perf_counter()
events = []


def on_press(key):
    events.append((key_to_string(key), "down", str(time.perf_counter() - start)))


def on_release(key):
    events.append((key_to_string(key), "up", str(time.perf_counter() - start)))
    if key == Key.esc:
        return False

    # if key_to_string(key) == "f":
    #     print(pyautogui.position())
    #     print("screenshot taken")
    #     screenshot = pyautogui.screenshot()
    #     screenshot.save("screen.png")


def save_input_to_file(inputs, file):
    file = open(file, "w")
    for inpt in inputs:
        file.write(", ".join(inpt) + "\n")
    file.close()


def record_input(file=DEFAULT_FILE):
    with Listener(on_press=on_press, on_release=on_release) as listener:
        global start
        global events
        wait_for_green_light()
        start = time.perf_counter()
        events = []
        listener.join()

    events = [event for event in events if event[0] in KEYS]

    to_remove = set()
    for i in range(len(events)):
        s = events[i]
        if s[1] == "up":
            continue

        for j in range(i + 1, len(events)):
            if s[0] == events[j][0]:
                if events[j][1] == "down":
                    to_remove.add(j)
                else:
                    break

    to_remove = list(to_remove)
    to_remove.reverse()
    for r in to_remove:
        events.pop(r)

    save_input_to_file(events, file)
    print(events)
