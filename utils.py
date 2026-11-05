def format_pace(pace):
    total_seconds = round(pace * 60)
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    return f"{minutes}:{seconds:02d} min/km"