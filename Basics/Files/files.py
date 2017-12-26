from os.path import dirname

file = open(dirname(__file__) + "\\" + "sample.txt", 'w')
file.write("hello again")
file.close()
