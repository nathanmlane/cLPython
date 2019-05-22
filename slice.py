def sillycase(word):
    half = int(len(word) / 2)
    first_half = word[:half].lower()
    last_half = word[half:].upper()
    return first_half + last_half

sillycase("apple")
