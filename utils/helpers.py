def format_duration(minutes: int) -> str:
    """Format minutes into HH:MM string."""
    hours, mins = divmod(minutes, 60)
    return f"{hours:02}:{mins:02}"
