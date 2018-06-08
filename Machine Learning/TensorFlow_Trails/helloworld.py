from tensorflow import Session, constant

someX = constant("Hello, TensorFlow!")

print(Session().run(someX))
