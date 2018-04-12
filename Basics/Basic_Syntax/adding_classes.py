class someClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return someClass(self.x + other.x, self.y + other.y)


if __name__ == "__main__":
    first = someClass(5, 7)
    second = someClass(3, 9)

    result = first + second

    print(result.x)
    print(result.y)
