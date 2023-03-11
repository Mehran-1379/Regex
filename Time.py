import re

input = input()

Time0 = re.search(r'0[0-9]:[0-5][0-9]' , input)

Time1 = re.search(r'1[0-9]:[0-5][0-9]' , input)

Time2 = re.search(r'2[0-3]:[0-5][0-9]' , input)

C = False

if Time0 != None :

    C = True

if Time1 != None :

    C = True

if Time2 != None :

    C = True

if C == True :

    print("True")

else :

    print("False")
