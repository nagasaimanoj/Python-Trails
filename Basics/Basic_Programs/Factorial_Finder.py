if __name__ == "__main__":
    num = int(input("enter a number to find it's factorial : "))

    result = 1

    if (num > 1):
        for i in range(1, num + 1):
            result *= i

    print(result)
