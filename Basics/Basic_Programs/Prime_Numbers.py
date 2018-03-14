n = int(input("Enter a number : "))

prime_numbers = []

for i in range(2, n):
    is_prime = True
    for j in range(2, i):
        if(i % j == 0):
            is_prime = False
    if(is_prime):
        prime_numbers.insert(len(prime_numbers), i)

if(prime_numbers):
    print(prime_numbers)
else:
    print("no prime numbers till", n)
