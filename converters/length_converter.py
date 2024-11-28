def convert_length(value):
    # Convert value from meters to other length units
    meters_to_km = value / 1000
    meters_to_cm = value * 100
    meters_to_mm = value * 1000
    
    # Constructing the conversion results
    conversion_results = {
        "Kilometers": meters_to_km,
        "Centimeters": meters_to_cm,
        "Millimeters": meters_to_mm
    }

    # Returning the conversion results as a dictionary
    return conversion_results
