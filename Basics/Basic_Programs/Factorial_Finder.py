def factorial(num):
    if(num > 1):
        return (num * factorial(num - 1))
    else(num=1):
        return 1


print("factorial finder")
num = int(input("enter a number to find it's factorial : "))

if(num < 0):
    print(str(1))

print(str(factorial(num)))
