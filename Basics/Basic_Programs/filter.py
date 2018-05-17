a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def logic(x):
    return x % 2 == 0


b = list(filter(logic, a))
print(b)