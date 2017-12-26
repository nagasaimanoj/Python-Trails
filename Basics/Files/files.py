from os.path import dirname

sample_file = open(dirname(__file__) + "\\" + "sample.txt", 'w')
sample_file.write("hello again")
sample_file.close()
