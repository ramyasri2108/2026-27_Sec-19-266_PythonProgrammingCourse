def sum_values(*args):
    total = 0
    for value in args:
        total += value
    return total

print(sum_values(1, 2, 3, 4, 5))
print(sum_values(10, 20, 30, 40, 60))
