from input_replayer import replay_input
from input_recorder import record_input
from utils import set_priority

if __name__ == "__main__":
    set_priority(priority=4)
    choice = input("press 'r' to record a run or press 'p' to replay a saved run: ")
    file = input("provide file path to override default one or press enter to continue: ")

    if choice == "r":
        if file != "":
            record_input(file)
        else:
            record_input()
    else:
        if file != "":
            replay_input(file)
        else:
            replay_input()
