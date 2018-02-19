# reading a number
num = int(input("enter a number : "))

# assuming the input number is a prime
is_prime = True

# for all positive numbers till input number, iterating loop
for j in range(2, num):

    # checking if iterating number can divide input number
    if(num % j == 0):
        # if current iterating number is able to divide input number, then it's not a prime forever
        is_prime = False
        break

# printing the primality of input number
print(is_prime)
