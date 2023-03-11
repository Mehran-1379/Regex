import re

input = input()

Check = re.search(r'[A-Z]+' , input)

if Check == None :

    print("True")

else :

    print("False")