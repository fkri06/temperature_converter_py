def celcius_to_fahrenheit(value):
    return value * (9 / 5) + 32

def celcius_to_kelvin(value):
    return value + 273.15

def fahrenheit_to_celcius(value):
    return (value - 32) * (5 / 9)

def fahrenheit_to_kelvin(value):
    return (value - 32) * (5 / 9) + 273.15

def kelvin_to_celcius(value):
    return value - 273.15

def kelvin_to_fahrenheit(value):
    return (value - 273.15) * (9 / 5) + 32
