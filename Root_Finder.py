from decimal import Decimal

num = Decimal(input("enter num : "))
root = Decimal(input("enter root : "))
mid_val = 0

if(root == 0): mid_val = 'undefined'
else:
    start = 0
    end = num

    result = 0
    mid_val = 0

    while(mid_val != (start + end) / 2):
        mid_val = (start + end) / 2
        result = mid_val**root

        if(result < num): start = mid_val
        if(result > num): end = mid_val

    if(mid_val == int(mid_val)): mid_val = int(mid_val)

print(str(root) + "√" + str(num) + " = " + str(mid_val))

input("\n\n----------\nHit enter to close\n")