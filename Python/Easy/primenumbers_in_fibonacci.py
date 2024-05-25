def primes_up_to(n: int) -> list[int]:
    return [x for x in range(2, n) if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]

def fibonacci_series(limit: int) -> list[int]:
    sequence = []
    a, b = 0, 1
    while a <= limit:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def prime_fibonacci_numbers(limit: int) -> list[int]:
    fibonacci_numbers = fibonacci_series(limit)
    prime_numbers = primes_up_to(limit)
    prime_fibonacci = [num for num in fibonacci_numbers if num in prime_numbers]
    return prime_fibonacci

print(prime_fibonacci_numbers(50))  # This will output Fibonacci numbers that are prime up to 50
