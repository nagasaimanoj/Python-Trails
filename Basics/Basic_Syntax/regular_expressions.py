from re import (findall,  # to find all occurances of a string in another string
                match,  # to return a bool if key matched with full string
                search)  # to return index of key in a full string

# getting full length string
inpstrng = input("input string : ")

# getting key to search in full length string
key = input("input key : ")

# checking if key matches with string
if match(key, inpstrng):
    print("re.match - Match")
else:
    print("re.match - No match")

# checking if string contains any substring that matches key
if search(key, inpstrng):
    print("re.search - Match")
else:
    print("re.search - No match")

# printing count of occurances of key in a string
print("re.findall - " + str(len(findall(key, inpstrng))))
