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

def replace(m):
    s = m.group(1)
    return '{}{}'.format(len(s), s[0])

def getAnswer(input, iterations = 1):
    input = input.replace("\r", "").split("\n")
    answer = ['',''] #part1, part2
    reg = re.compile(r'((\d)\2*)')
    input = str(input)
    for i in range(iterations):
        input = reg.sub(replace, input)
        if i == iterations - 11:
            answer[0] = len(input)

    #answer[0] = len(input)
    answer[1] = len(input)
    return answer

# while(True):
#     ans = getAnswer(menu())
#     print(ans)

print(getAnswer('1113222113', 50))