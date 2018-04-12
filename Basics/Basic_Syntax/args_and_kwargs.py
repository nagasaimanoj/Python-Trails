def someLogic(var1, var2, *vars, **key_args):
    print(var1)
    print(var2)
    print(vars)
    print(key_args)


if __name__ == "__main__":
    someLogic(1, 12, "manoj", "kumar", name="kumar", age="22")
