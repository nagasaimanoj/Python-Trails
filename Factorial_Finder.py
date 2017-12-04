def factorial(num):
    if(num > 1 ):   return (num * factorial(num - 1))
    else:   return 1
    
print("factorial finder")
num = int(input("enter a number to find it's factorial : "))

print(str(factorial(num)))

input("\n\n----------\nHit enter to close\n")