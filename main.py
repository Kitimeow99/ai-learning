runner_name = input("Runner name: ")

try:
    distance_km = float(input("Distance in km: "))
    duration_minutes = float(input("Duration in minutes: "))
    if distance_km <= 0 or duration_minutes <= 0:
        print("Distance and duration must be greater than zero.")
    else:
        pace = duration_minutes / distance_km

        print(f"\nRunner: {runner_name}")
        print(f"Distance: {distance_km} km")
        print(f"Time: {duration_minutes} minutes")
        print(f"Average Pace: {pace:.2f} min/km")

except ValueError:
    print("Please enter numbers for distance and duration.")
