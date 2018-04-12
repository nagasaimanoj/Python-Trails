from subprocess import call

if __name__ == "__main__":
    file = input(r"drop a python file here : ")

    call(['python', file])
