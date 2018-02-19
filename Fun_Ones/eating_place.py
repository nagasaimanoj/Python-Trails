from random import randint

def choose_a_place():
    options = int(input("how many options do you have ? : "))
    describe = input("do you want to name them...? (y/n) : ")

    if(describe in ('y', 'Y')):
        a = {}
        for i in range(options):
            a[i] = input("enter an option : ")
        print("go with " + a[randint(1, options - 1)])
    elif(describe in ('n', 'N')):
        print("go with option " + str(randint(1, options - 1)))

while(True):
    choose_a_place()
    again = input("do you want to choose again..? (y/n) : ")
    if(again == 'n'):
        break
