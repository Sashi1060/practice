def factorial_of_number(number: int) -> int:
    return 1 if number == 0 else number * factorial_of_number(number - 1)

print(factorial_of_number(6))  # Expected output: 120
