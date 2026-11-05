import csv

from utils import format_pace

distances = []
durations = []

runner_name = input("Runner name: ")

while True:
    distance_text = input("\nDistance in km (or q to finish): ")

    if distance_text.lower() == "q":
        break

    try:
        distance_km = float(distance_text)
        duration_minutes = float(input("Duration in minutes: "))

        if distance_km <= 0 or duration_minutes <= 0:
            print("Distance and duration must be greater than zero.")
            continue

        distances.append(distance_km)
        durations.append(duration_minutes)

        pace = duration_minutes / distance_km
        print(f"Run added. Pace: {format_pace(pace)}")

    except ValueError:
        print("Please enter valid numbers.")

if distances:
    total_distance = sum(distances)
    total_duration = sum(durations)
    average_pace = total_duration / total_distance

    print(f"\nSummary for {runner_name}")
    print(f"Runs recorded: {len(distances)}")
    print(f"Total distance: {total_distance:.2f} km")
    print(f"Total duration: {total_duration:.2f} minutes")
    print(f"Overall pace: {format_pace(average_pace)}")
else:
    print("No runs recorded.")

if distances:
    with open("runs.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(["runner", "distance_km", "duration_minutes"])

        for distance, duration in zip(distances, durations):
            writer.writerow([runner_name, distance, duration])

    print("Runs saved to runs.csv")