import sys
import os
import re

def readFile(path):
    f = open(path, "r")
    return f.read().strip()

def menu():
    main = "\nPlease choose an input option:\n"
    main += "1. Text File\n"
    main += "2. Prompt\n"
    main += "3. Quit\n"
    main += ">> "
    choice = input(main)
    if choice == "3":
        sys.exit(0)
    if choice not in ["1","2"]:
        print("Invalid option. Try Again.\n")
        return menu()
    else:
        if choice == "1":
            return readFile(input("File Name: "))
        else:
            return input("Input: ")

def incPass(pwd):
    a = [*pwd]
    #print(a)
    i = len(a)-1
    #print(i)
    while i >= 0:
        o = ord(a[i])
        o += 1
        if o > 122:
            a[i] = 'a'
            i -= 1
            #print('incPass dec')
        else:
            a[i] = chr(o)
            #print('incPass break: {}:{}'.format(i, a[i]))
            break
    
    #print(a)
    newPass = ''.join(a)
    #print('incPass returning {}'.format(newPass))
    return newPass

def passIsValid(pwd):
    if len(pwd) != 8: return False
    for c in pwd:
        o = ord(c)
        if o < 97 or o > 122: 
            #print('passIsValid char invalid')
            return False
        if c == 'i' or c == 'o' or c == 'l': 
            #print('passIsValid has i/o/l')
            return False
    reg = re.compile(r'([a-z])\1')
    d = {}
    for m in re.finditer(reg, pwd):
        d[m.group(1)] = True
    if len(d.keys()) < 2: 
        #print('passIsValid < 2 dupes')
        return False

    for i in range(6):
        o = ord(pwd[i])
        if ord(pwd[i+1]) == o+1 and ord(pwd[i+2]) == o+2: 
            #print('passIsValid return true')
            return True

    #print('passIsValid no straight')
    return False

def getNewPass(input):
    newPwd = incPass(input)
    while passIsValid(newPwd) == False:
        newPwd = incPass(newPwd)
    return newPwd

def getAnswer(input):
    if '\r' in input or '\n' in input:
        input = input.replace("\r", "").split("\n")
    answer = ['',''] #part1, part2
    
    answer[0] = getNewPass(input)
    answer[1] = getNewPass(answer[0])
    return answer

# while(True):
#     ans = getAnswer(menu())
#     print(ans)

print(getAnswer('cqjxjnds'))