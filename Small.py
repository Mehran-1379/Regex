import re

input = input()

Check = re.search(r'function [A-Z]+[a-z]*[A-Z]*' , input)

if Check == None :

    print("True")

else :

    print("False")