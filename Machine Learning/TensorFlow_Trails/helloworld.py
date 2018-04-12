from tensorflow import (Session, constant)

if __name__ == "__main__":
    someX = constant("Hello, TensorFlow!")

    print(Session().run(someX))
