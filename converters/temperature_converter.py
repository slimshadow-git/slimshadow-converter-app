def convert_temperature(value):
    # Convert value from Celsius to other temperature units
    celsius_to_fahrenheit = (value * 9/5) + 32
    celsius_to_kelvin = value + 273.15
    
    # Constructing the conversion results
    conversion_results = {
        "Fahrenheit": celsius_to_fahrenheit,
        "Kelvin": celsius_to_kelvin
    }

    # Returning the conversion results as a dictionary
    return conversion_results
