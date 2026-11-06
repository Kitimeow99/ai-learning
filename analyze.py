import csv
from utils import format_pace, summarize_runs


try:
    with open("runs.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        totals = summarize_runs(reader)

    if not totals:
        print("No saved runs found.")

    for name, stats in totals.items():
        pace = stats["duration"] / stats["distance"]

        print(f"\nRunner: {name}")
        print(f"Runs: {stats['runs']}")
        print(f"Total distance: {stats['distance']:.2f} km")
        print(f"Total duration: {stats['duration']:.2f} minutes")
        print(f"Overall pace: {format_pace(pace)}")

except FileNotFoundError:
    print("No runs.csv found. Run main.py and save a run first.")