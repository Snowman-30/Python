## lists  ->  Mutable

# a = [4, True, "abc"]
# y = "hi"
# # print(len(a), len(y))
# # b = a             # Exact elements stored | Changes in a affects b
# b = a[:]  # Original elements stored |Copy of a in b
# a.append("Hello")
# a.extend([4, 5, 6, 4, 8])
# a.pop()
# a.pop(2)
# a[0] = "bye"

# print(a, b)

# # Tuples    ->  Immutable.

# t = (69, 110, 106)
# # t.append(5)
# print(t)


# x = [[], (), [[], [], ()], ((), [])]    # Possible


# Slice

a = [0, 1, 2, 3, 4, 5, 6]
b = ["hi", "Hello", "cya", "bye"]
c = "Hello"

sliced = a[0:90:2]

print(sliced)


a = [5, 4, 3, 2, 1]
b = a.copy()
a.append(69)
print(a, b)
