def print_Fizz_Buzz(num):
    for i in range(1, num + 1):
        text = str(i)
        if(i % 3 == 0):
            text += " - Fizz"
        if(i % 5 == 0):
            text += " - Buzz"
        print(text)


print_Fizz_Buzz(int(input("Enter range : ")))
