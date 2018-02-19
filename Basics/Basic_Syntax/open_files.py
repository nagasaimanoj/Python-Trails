from subprocess import call  # to run a terminal command

# getting a file's path and name
file = input(r"drop a python file here : ")

# running terminal script on that file
call(['python', file])
