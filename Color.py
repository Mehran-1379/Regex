import re

input = input()

Color = re.search(r'# [A-F]|[0-9][A-F]|[0-9][A-F]|[0-9][A-F]|[0-9][A-F]|[0-9][A-F]$|[0-9]$' , input)

if Color != None :

    print("True")

else :

    print("False")