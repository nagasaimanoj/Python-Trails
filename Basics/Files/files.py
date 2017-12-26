import os

file = open(os.path.dirname(__file__) + "\\" + "sample.txt", 'w')
file.write("hello again")
file.close()