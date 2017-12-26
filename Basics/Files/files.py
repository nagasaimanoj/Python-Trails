from os.path import dirname

SAMPLE_FILE = open(dirname(__file__) + "\\" + "sample.txt", 'w')
SAMPLE_FILE.write("hello again")
SAMPLE_FILE.close()
