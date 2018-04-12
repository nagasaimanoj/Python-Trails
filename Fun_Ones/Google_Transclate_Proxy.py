from os import startfile

if __name__ == "__main__":
    path = "https://translate.google.com/translate?u="
    variables = "&anno=2&hl=en&sl=en&tl=en"
    url = input("enter website url : ")

    startfile(path + url + variables)
