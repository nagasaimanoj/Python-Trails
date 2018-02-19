# reading a number
num = int(input("enter a number to find it's factorial : "))

# initialising result as 1
result = 1

# checking if input number is greater than 1
if(num > 1):
    # multiplying every positive number till input number
    for i in range(1, num + 1):
        result *= i

# printing the factorial for input number
print(result)
