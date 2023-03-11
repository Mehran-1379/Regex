import re

input = input()

Color = re.search(r'#\s*[A-F 0-9]{6}' , input)

if Color != None :

    print("True")

else :

    print("False")