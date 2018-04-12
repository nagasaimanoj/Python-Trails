class grand_parent:
    def __init__(self):
        print("from grand_parent")


class parent(grand_parent):
    def __init__(self):
        print("from parent")


class child(parent):
    def __init__(self):
        print("from child")


if __name__ == "__main__":
    obj = child()
