from tensorflow import (Session,  # to start TF session
                        constant)  # to declare constant variables

# creating a constant variable someX
someX = constant("Hello, TensorFlow!")

# running that variable using a session, this will return variable's value. we're printing it
print(Session().run(someX))
