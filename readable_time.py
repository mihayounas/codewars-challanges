def make_readable(seconds):
    # Do something
    if seconds > 359999:
        raise ValueError("Invalid input. Maximum time exceeded.")
    
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"