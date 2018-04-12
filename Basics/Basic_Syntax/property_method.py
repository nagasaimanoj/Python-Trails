class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False


if __name__ == "__main__":
    pizza = Pizza(["cheese", "tomato"])
    print(pizza.pineapple_allowed)
    pizza.pineapple_allowed = True
