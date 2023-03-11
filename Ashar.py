import re

input = input()

Check = re.search(r'\d+\.', input)

if Check == None :
    print("False")
else :
    print("True")
