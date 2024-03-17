def generate_integers(a, b):
    """
    Do positive integers a aur b diye gaye hain, a aur b ke beech ke even digits ko ascending order mein return karo.

    Jaise ki:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        return []
    if a == b:
        return [a]
    if a > 0 and b > 0:
        return [a, a + 2, a + 4, a + 6, a + 8]
    if a > 0 and b < 0:
        return [a, a + 2, a + 4, a + 6, a + 8]
    if a < 0 and b > 0:
        return [a, a + 2, a + 4, a + 6, a + 8]
    if a < 0 and b < 0:
        return []


print(generate_integers(2, 8))
print(generate_integers(8, 2))
print(generate_integers(10, 14))
