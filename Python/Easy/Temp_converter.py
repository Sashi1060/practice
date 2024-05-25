def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5/9

print(celsius_to_fahrenheit(25)) 

# Expected output: 77.0 Fahrenheit
print(fahrenheit_to_celsius(77)) 

# Expected output: 25.0 Celsius
