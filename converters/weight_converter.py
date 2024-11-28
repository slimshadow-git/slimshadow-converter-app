def convert_weight(value):
    # Convert value from kilograms to other weight units
    kg_to_g = value * 1000
    kg_to_mg = value * 1_000_000
    kg_to_ton = value / 1000
    
    # Constructing the conversion results
    conversion_results = {
        "Grams": kg_to_g,
        "Milligrams": kg_to_mg,
        "Tons": kg_to_ton
    }

    # Returning the conversion results as a dictionary
    return conversion_results
