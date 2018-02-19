# reading input number
num = int(input("Enter range : "))

# for each positive number till input number, running the loop
for i in range(1, num + 1):
    # assigning default output value as the current iterating number
    text = str(i)

    # checking if the number is multiple of 3 to append 'Fizz' to output string
    if(i % 3 == 0):
        text += " - Fizz"

    # checking if the number is multiple of 5 to append 'Buzz' to output string
    if(i % 5 == 0):
        text += " - Buzz"

    # printing current iterating number & corrosponding word
    print(text)
