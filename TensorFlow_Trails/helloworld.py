from tensorflow import constant, Session

# creating Session to run a s'tring. this will print it's value
print(Session().run(constant("Hello, TensorFlow!")))
