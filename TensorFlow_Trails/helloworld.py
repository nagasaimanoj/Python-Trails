from tensorflow import constant, Session

print(Session().run(constant('Hello, TensorFlow!')))
