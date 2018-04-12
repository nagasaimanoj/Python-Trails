class Animal:
    def sound(self):
        raise NotImplementedError("Logic Not Implemented")

    def name(self):
        raise NotImplementedError("Logic Not Implemented")


class Dog(Animal):
    def sound(self):
        print("bow - bow")

    def name(self):
        print("scooby")


try:
    object = Animal()
    object.sound()
    object.name()
except Exception as e:
    print(e)
else:
    print("else block")
finally:
    print("finally block")

try:
    object = Dog()
    object.sound()
    object.name()
except Exception as e:
    print(e)
else:
    print("else block")
finally:
    print("finally block")
