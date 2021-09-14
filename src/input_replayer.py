import time

from pynput.keyboard import Listener, Controller

from utils import DEFAULT_FILE, key_to_string, wait_for_green_light, KEYS
from windows_input import press_key, release_key

keyboard = Controller()


def read_input_file(file) -> [(str, str, float)]:
    result = []
    file = open(file, "r")
    for line in file:
        values = line.strip().split(", ")
        values[2] = float(values[2])
        result.append(values)

    return result


def on_release(key):
    if key_to_string(key) == "s":
        return False


def wait_for_input():
    with Listener(on_release=on_release) as listener:
        listener.join()


def handle_action(action):
    if action[1] == "down":
        press_key(action[0].upper())
    else:
        release_key(action[0].upper())


def replay_actions(actions: list[(str, str, float)]) -> None:
    start = time.perf_counter()
    press_key(KEYS[0])
    while len(actions):
        action = actions.pop(0)
        while action[2] + 0.07 > time.perf_counter() - start:
            pass

        handle_action(action)
        # print(time.perf_counter() - start - action[2], action)


def replay_input(file=DEFAULT_FILE):
    inputs = read_input_file(file)
    print("waiting for user input...")
    wait_for_input()
    print("waiting for green light...")
    wait_for_green_light()
    replay_actions(inputs)
    print("finished")
