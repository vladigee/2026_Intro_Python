
def to_kelvin(temp_celsius):
    if temp_celsius < -273.15:
        raise ValueError("below absolute zero")
    return temp_celsius + 273.15
