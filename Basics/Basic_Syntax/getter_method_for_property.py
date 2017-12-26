class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    self._pineapple_allowed = False

  @property
  def pineapple_allowed(self):
    return self._pineapple_allowed

  @pineapple_allowed.setter
  def pineapple_allowed(self, value):
    self._pineapple_allowed = value

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)

pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)

pizza.pineapple_allowed = False
print(pizza.pineapple_allowed)