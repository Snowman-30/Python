vowels = set("aeiou")


def check(s):
    count = 0
    for ch in s.lower():
        if ch.isalpha() and ch in vowels:
            count += 1
    return print(count)


check("Hello")
