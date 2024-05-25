def length_of_lastword(sentence: str) -> int:
    return len(sentence.split()[-1]) if sentence.split() else 0

print(length_of_lastword("I am Sashi")) 
# Expected output: 5
