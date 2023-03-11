import re

input = input()

Cho = re.search(r'chocolate' , input)

if Cho == None :
   
    print("True")

else :

    print("False")