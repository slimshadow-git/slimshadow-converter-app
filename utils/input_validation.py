def validate_input(value):
    try:
        # Try to convert the input value to a float
        float(value)
        return True
    except ValueError:
        # If conversion fails, it's not a valid number
        return False
