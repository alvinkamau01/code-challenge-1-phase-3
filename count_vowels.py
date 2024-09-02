def count_vowels(text):
    vowels = "aeiou"
    count = sum(1 for char in text.lower() if char in vowels)
    return count