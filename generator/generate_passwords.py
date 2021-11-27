import random

charList = input("Enter a list of characters to be used or leave blank to use the default: ")

charList = charList if charList else "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-_ @*"

pswdList = open("passwords.txt", 'w')

if input("Should the common passwords be appended? (Leave blank for no) "):
    pswdList.write(open("common_passwords.min.txt").read())

validInput = False;
while not validInput:
    try:
        validInput = True
        for i in range(int(input("How many passwords should be generated? "))):
            for j in range(random.randrange(8, 13)):
                pswdList.write(charList[random.randrange(len(charList))])
            pswdList.write('\n')
    except ValueError:
        validInput = False
pswdList.close()
