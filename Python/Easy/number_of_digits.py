def number_of_digits(number: int) -> int:
    return len(str(abs(number)))

print(number_of_digits(-12345))