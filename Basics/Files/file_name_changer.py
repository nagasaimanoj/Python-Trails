from os import (listdir,  # displays folder's contents
                rename)  # to rename files

for file_name in listdir():
    new_name = file_name[4:]
    rename(file_name, new_name)
