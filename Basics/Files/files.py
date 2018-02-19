from os.path import dirname  # to get current python file's path

SAMPLE_FILE = open(dirname(__file__) + "\\" + "sample.txt", 'w')
SAMPLE_FILE.write("hello again")
SAMPLE_FILE.close()
