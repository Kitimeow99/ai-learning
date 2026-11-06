def format_pace(pace):
    total_seconds = round(pace * 60)
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    return f"{minutes}:{seconds:02d} min/km"

def summarize_runs(rows):
    totals = {}

    for row in rows:
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


    return totals