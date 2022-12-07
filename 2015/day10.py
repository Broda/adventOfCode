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

def getNextSequence(curr):
    next = ''
    start = 0
    end = 1
    while start < len(curr):
        c = curr[start]
        while end < len(curr) and curr[end] == c:
            end += 1
        next += '{}{}'.format(end - start, c)
        start = end
        end += 1

    return next

def getAnswer(input, iterations = 1):
    input = input.replace("\r", "").split("\n")
    answer = ['',''] #part1, part2
    for i in range(iterations):
        input = getNextSequence(input)
    answer[0] = len(input)
    answer[1] = ''
    return answer

# while(True):
#     ans = getAnswer(menu())
#     print(ans)
#print(getAnswer('1',5))
# print(getAnswer('11'))
# print(getAnswer('21'))
# print(getAnswer('1211'))
# print(getAnswer('111221'))
print(getAnswer('1113222113', 40))