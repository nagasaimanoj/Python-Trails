n = int(input("Enter a number : "))
prime_factors = []

for i in range(2, n):
    is_prime = True
    for j in range(2, i):
            if(i % j == 0): is_prime = False
    if(is_prime and n % i == 0):
        prime_factors.insert(len(prime_factors), i)

if(len(prime_factors)):
    for i in range(len(prime_factors)):
        print(str(prime_factors[i]) + " x " + str(int(n / prime_factors[i])))

else:
    print("Error : no prime factors for " + str(n))

input("\n\n----------\nHit enter to close\n")