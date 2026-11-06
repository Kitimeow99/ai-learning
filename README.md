# Python Running Tracker

A beginner Python project for recording running activities
and calculating totals for each runner.

## Features

- Enter multiple runs with input validation
- Save activities to CSV
- Calculate each runner's total distance and duration
- Display pace as minutes and seconds per kilometre
- Test pace formatting automatically

## Requirements

Python 3. No additional packages required.

## Usage

Run these commands from the project folder.

Record activities:

```bash
python main.py
```

Enter q at the distance prompt to finish and save.

Analyze saved activities:

```bash
python analyze.py
```

Run tests:

```bash
python -m unittest -v
```

## Files

- main.py: enter and save runs
- analyze.py: summarize saved runs by runner
- utils.py: shared pace formatting function
- test_utils.py: pace formatting tests

runs.csv is created when activities are saved and is excluded from Git.

## Current limitations

- Runner names must match exactly to be grouped together.
- The analyzer expects valid CSV records created by main.py.
- Activities are saved when the user finishes with q.