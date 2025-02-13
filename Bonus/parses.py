def parse(feet_inches):
    """Calculate the feet and inches before print the result
        in meters"""
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches
