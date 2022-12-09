import sys
import os
import re
import json

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

def findRed(dict):
    reg = re.compile(r'{([^}]*)}') #r'({[^{}]*red[^{}]*})')
    input = re.sub(reg, '', input)
    for k in dict.keys():
        print('{}={}'.format(k, dict[k]))

def getAnswer(input):
    if '\r' in input or '\n' in input:
        input = input.replace("\r", "").split("\n")
        input = ''.join(input)
    answer = ['',''] #part1, part2
    
    reg = re.compile(r'(-?[\d]+)')
    sum = 0
    for num in re.findall(reg, input):
        sum += int(num)
    
    j = json.loads(input)
    findRed(j[0])

    answer[0] = sum
    answer[1] = ''
    return answer

while(True):
    ans = getAnswer(menu())
    print(ans)
