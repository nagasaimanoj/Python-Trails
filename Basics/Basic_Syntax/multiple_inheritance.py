class parent1:
  def __init__(self):
    print("parent1")

class parent2:
  def __init__(self):
    print("parent2")

class child(parent2, parent1):
  pass

obj = child()
