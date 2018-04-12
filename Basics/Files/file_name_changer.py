from os import (listdir, rename)

if __name__ == "__main__":
    for file_name in listdir():
        new_name = file_name[4:]
        rename(file_name, new_name)
