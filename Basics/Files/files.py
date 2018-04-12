from os.path import dirname

if __name__ == "__main__":
    SAMPLE_FILE = open(dirname(__file__) + "\\" + "sample.txt", 'w')
    SAMPLE_FILE.write("hello again")
    SAMPLE_FILE.close()