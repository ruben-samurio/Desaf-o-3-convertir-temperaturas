def celsius_a_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin


celsius = 25
kelvin =celsius_a_kelvin(celsius)

print(f"{celsius}ºC equivalen a {kelvin}K")