import os

path = "https://translate.google.com/translate?u="
variables = "&anno=2&hl=en&sl=en&tl=en"
url = input("enter website url : ")

os.startfile(path + url + variables)

input("\n\n----------\nHit enter to close\n")