# Trackmania Run Replaying Tool


## Disclaimer

<p style="color:red">
    The following program is a proof of concept of a high level tool that can record and replay a set of inputs used to perform a run in Trackmania Nations Forever.
    <br/>
    Unfortunately manual testing shows that while the tool is able to closely replicate runs on the short tracks the deviation from the original path becomes significant enough to disqualify reliable use for runs with duration of over 10 seconds.
</p>

## Description

Trackmania Run Replaying Tool is an attempt to leverage determinism of the driving model in Trackmania games by providing an option to record and replay the user input.  

## Installation

Clone this repository:

```bash
git clone https://github.com/przemo199/trackamania-run-replaying-tool
```

You will also need Python 3 (no guarantee it will run on anything older than Python 3.9) to run this tool.

## Usage

The control buttons accepted by default are: `W`, `S`, `A`, `D`, `R`, `Esc`, `Shift` and `Delete`, other pressed buttons are discarded from logs after the recording is finished.  
The list of accepted buttons can be modified by changing the list `KEYS` in `./src/utils.py`  
NOTE: At least one button used for accelerating must be placed at the index `0` of the list as the tool uses it to ensure that no delay occurs at the beginning of the run.  

The tool is not designed to handle in-game pause, avoid pressing `Esc` before you finish the run as the tool will stop recording.  

To start the tool run ```main.py``` and follow the instructions of the CLI.  
