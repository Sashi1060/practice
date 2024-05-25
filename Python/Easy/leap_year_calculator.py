def leap_year_calculator(year: int) -> bool:
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(leap_year_calculator(2020))  # Expected output: True
print(leap_year_calculator(1900))  # Expected output: False
print(leap_year_calculator(2000))  # Expected output: True
