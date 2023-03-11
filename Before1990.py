import re

input = input()

C = False

Year1 = re.search(r'\((199\d+)' , input)

Year2 = re.search(r'\((2\d{3})' , input)

if Year1 != None :

    C = True

if Year2 != None :

    C = True

if C != True :

    print("True")
    
else :

    print("False")
