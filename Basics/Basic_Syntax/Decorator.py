# this functoin is decorator
def someXlogic(someFunc):
    # this has to return an object or function. so defining one
    def someOtherFunc(x, y):
        print("prior to actual logic")
        someFunc(x, y)
        print("after my actual logic")
        # returning an object

    return someOtherFunc


# defining a functoin with decorator. this will run our functoin with decorators rules
@someXlogic
def myLogic(a, b):
    print(a + b)


# calling in normal way. but decorator will get involved
myLogic(1, 2)
