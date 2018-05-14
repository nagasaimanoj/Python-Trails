class SampleClass:
    def some_method(self):
        print("1st method")

    def some_method(self, var1):
        print("2nd method")

    def some_method(self, var1, *var2):
        print("3rd method")


obj = SampleClass()

obj.some_method(1, 2)
obj.some_method(1)
obj.some_method()