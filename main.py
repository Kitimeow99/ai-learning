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
        print(f"Run added. Pace: {pace:.2f} min/km")

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
    print(f"Overall pace: {average_pace:.2f} min/km")
else:
    print("No runs recorded.")