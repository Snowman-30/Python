# 1. Sum of Even numbers.
# **************************************************************************************************************

# 2025-10-15 — E1 Sum evens
# Bug: NameError because accumulator not initialized.
# Fix: add total = 0 before loop.
# Lesson: Always initialize accumulators; test [] case.

# **************************************************************************************************************

# a = [1, 2, 3, 4]
a = [1, 2, 3, 4, 5, 6, 8, 9, 7, 8, 5, 4, 3, 21]
# a = []
total = 0
for i in a:
    if i % 2 == 0:
        total += i

print(total)