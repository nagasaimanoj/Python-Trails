class Person:

    @property
    def val(self):
        pass

    @val.setter
    def val(self, val):
        print("@val.setter called")
        self._val = val

    @val.getter
    def val(self):
        print("@val.getter called")
        return self._val


p = Person()
p.val = 30
print(p.val)
