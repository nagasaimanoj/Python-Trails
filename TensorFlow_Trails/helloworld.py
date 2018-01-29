from tensorflow import (Session,  # to start TF session
                        constant)  # to declare constant variables

# creating Session to run a s'tring. this will print it's value
print(Session().run(constant("Hello, TensorFlow!")))
