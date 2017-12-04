import re

inpstrng = input("input string : ")
key = input("input key : ")

if(re.match(key, inpstrng)):
    print("re.match - Match")
else:
   print("re.match - No match")

if re.search(key, inpstrng):
   print("re.search - Match")
else:
   print("re.search - No match")
    
print("re.findall - " + str(len(re.findall(key, inpstrng))))

input("\n\n----------\nHit enter to close\n")