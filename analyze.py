import csv

totals = {}

try:
    with open("runs.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row["runner"]
            distance = float(row["distance_km"])
            duration = float(row["duration_minutes"])

            if name not in totals:
                totals[name] = {
                    "runs": 0,
                    "distance": 0.0,
                    "duration": 0.0
                }

            totals[name]["runs"] += 1
            totals[name]["distance"] += distance
            totals[name]["duration"] += duration

    if not totals:
        print("No saved runs found.")

    for name, stats in totals.items():
        pace = stats["duration"] / stats["distance"]

        print(f"\nRunner: {name}")
        print(f"Runs: {stats['runs']}")
        print(f"Total distance: {stats['distance']:.2f} km")
        print(f"Total duration: {stats['duration']:.2f} minutes")
        print(f"Overall pace: {pace:.2f} min/km")

except FileNotFoundError:
    print("No runs.csv found. Run main.py and save a run first.")