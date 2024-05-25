def is_palindrome(word: str) -> str:
    return True if word.lower() == word.lower()[::-1] else False

print(is_palindrome("Madam"))