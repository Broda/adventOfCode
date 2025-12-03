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

def getCodeCharCount(s):
    len_s = len(s)
    #print(f"getCodeCharCount({s}) = {len_s}")
    return len_s

def getMemCharCount(s):
    len_s = len(s.encode('utf-8').decode('unicode-escape'))-2
    #print(f"getMemCharCount({s}) = {len_s}")
    return len_s

def getEncodeCharCount(s):
    new_s = s.replace("\\", "\\\\")
    new_s = new_s.replace("\"", "\\\"")

    print(new_s)
    len_s = len(new_s)+2
    print(f"getEncodeCharCount({s}) = {len_s}")
    return len_s

def getAnswer(input):
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2
    for l in input:
        answer[0] += (getCodeCharCount(l) - getMemCharCount(l))
        answer[1] += (getEncodeCharCount(l) - getCodeCharCount(l))
    return answer

while(True):
    ans = getAnswer(menu())
    print(ans)
