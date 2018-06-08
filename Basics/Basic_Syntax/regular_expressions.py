from re import findall, match, search

inpstrng = input("input string : ")

key = input("input key : ")

if match(key, inpstrng):
    print("re.match - Match")
else:
    print("re.match - No match")

if search(key, inpstrng):
    print("re.search - Match")
else:
    print("re.search - No match")

print("re.findall - " + str(len(findall(key, inpstrng))))
