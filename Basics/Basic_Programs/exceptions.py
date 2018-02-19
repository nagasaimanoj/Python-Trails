# try - except block to handle exceptions
try:
    # using un-assigned variable to raise exception
    a = 10 / x
    print("hello")
except:
    # this will run if exception happened
    print("except block")
else:
    # this will run if exception didn't occoured
    print("else block")
finally:
    # this will run no matter if exception occoured or not
    print("finally block")
