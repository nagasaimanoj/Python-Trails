def inc(x):
    return x + 1


def failure_case():
    assert inc(3) == 5


def success_case():
    assert inc(4) == 5


if __name__ == '__main__':
    success_case()
    failure_case()
