set_vowels = set("aeiou")


def vowels(s):
    count = 0
    for ch in s.lower():
        if s.isalpha() and ch in set_vowels:
            count += 1
    return count


print(vowels("a e i o u"))
