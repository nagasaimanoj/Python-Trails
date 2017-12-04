import itertools

num = int(input("enter a number : "))

is_prime = True

for j in range(2, num):
        if(num % j == 0):
                is_prime = False
                break

print(is_prime)

input("\n\n----------\nHit enter to close\n")