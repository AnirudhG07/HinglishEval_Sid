
def even_odd_palindrome(n):
    """
    Ek positive integer n diya gaya hai, return karo ek tuple jisme even aur odd integer palindromes ki sankhya ho jo range(1, n) ke andar aate hain, inclusive.

    Udaharan 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome hain 1, 2, 3. Inme se ek even hai, aur do odd hain.

    Udaharan 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome hain 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. Inme se chaar even hain, aur 6 odd hain.

    Dhyan de:
        1. 1 <= n <= 10^3
        2. returned tuple me even aur odd integer palindromes ki sankhya kramashah hoti hai.
    """
    return ([i for i in range(1, n + 1) if str(i) == str(i)[::-1]
             and i % 2 == 1]
            or [i for i in range(2, n + 1) if str(i) == str(i)[::-1] and i % 2 == 0])


print("\n\n")
print("\t\t\t\tQuestion 22")
print("\t\t\t\t----")
print("\n")

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
