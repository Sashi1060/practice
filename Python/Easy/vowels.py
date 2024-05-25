def count_vowels(word: str) -> int:
    vowels = "aeiouAEIOU"  # List of vowels, both lowercase and uppercase
    return sum(1 for char in word if char in vowels)  # Count and sum the vowels in the word

print(count_vowels("Sashi"))  # Expected output: 2
