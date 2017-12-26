import subprocess

file = input(r"drop a python file here : ")

subprocess.call(['python', file])