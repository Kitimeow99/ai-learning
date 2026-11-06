import math

def format_pace(pace):
    total_seconds = round(pace * 60)
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    return f"{minutes}:{seconds:02d} min/km"

def summarize_runs(rows):
    totals = {}
    skipped = 0

    for row in rows:
        try:
            name = row["runner"].strip()
            distance = float(row["distance_km"])
            duration = float(row["duration_minutes"])

            if not name:
                raise ValueError("Runner name is empty")

            if not math.isfinite(distance) or not math.isfinite(duration):
                raise ValueError("Values must be finite")

            if distance <= 0 or duration <= 0:
                raise ValueError("Values must be positive")

        except (ValueError, TypeError, KeyError, AttributeError):
            skipped += 1
            continue

        if name not in totals:
            totals[name] = {
                "runs": 0,
                "distance": 0.0,
                "duration": 0.0
            }

        totals[name]["runs"] += 1
        totals[name]["distance"] += distance
        totals[name]["duration"] += duration

    return totals, skipped