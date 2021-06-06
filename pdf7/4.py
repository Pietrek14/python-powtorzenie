def zlicz_znaki_alfanumeryczne(tekst):
    if not isinstance(tekst, str):
        print("Podana zmienna nie jest tekstem!")
        return None
    result = {}
    tekst = tekst.lower()
    for char in tekst:
        if char.isalnum():
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
    return result

print(zlicz_znaki_alfanumeryczne("The quick brown fox jumps over a lazy dog."))