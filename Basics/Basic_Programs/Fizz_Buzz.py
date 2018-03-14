num = int(input("Enter range : "))

for i in range(1, num + 1):
    result = str(i)

    if(i % 3 == 0):
        result += " - Fizz"

    if(i % 5 == 0):
        result += " - Buzz"

    print(result)
