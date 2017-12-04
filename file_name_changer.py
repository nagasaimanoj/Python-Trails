import os

for file_name in os.listdir():
    new_name = file_name[4:]
    os.rename(file_name, new_name)