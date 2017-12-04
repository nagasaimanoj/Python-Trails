def dashes(func):
    def someFun():
        print("-=-=-=-=-=-")
        func()
        print("-=-=-=-=-=-")
    return someFun

def someY(func):
    def someFun():
        print("**********")
        func()
        print("**********")
    return someFun

@someY
def someX():
    print("someX")

someX()

input("\n\n----------\nHit enter to close\n")