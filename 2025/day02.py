import os
import sys
import re

def menu():
    main = "\nPlease choose an input option:\n"
    main += "1. Sample File\n"
    main += "2. Input File\n"
    main += "3. Other File\n"
    main += "4. Prompt\n"
    main += "5. Quit\n"
    main += ">> "
    
    filename = os.path.basename(__file__)
    samplePath = filename.replace('.py', 'sample.txt')
    inputPath = filename.replace('.py', 'input.txt')
    
    match input(main):
        case "5":
            sys.exit(0)
        case "1":
            isSample = True
            return readFile(samplePath), True
        case "2":
            return readFile(inputPath), False
        case "3":
            return readFile(input("File Name: ")), False
        case "4":
            return input("Input: "), False
        case _:
            print("Invalid option. Try Again.\n")
            return menu()

def readFile(path):
    if not os.getcwd().endswith('2025'): os.chdir('2025')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2025'): os.chdir('2025')
    f = open(path, 'w')
    f.write(s)
    f.close()

def isInvalidID(numAsStr : str, patt : str = r"^(.+)\1$") -> bool:
    match = re.search(patt, numAsStr)
    return match is not None

def getInvalidSum(input, patt : str = r"^(.+)\1$") -> int:
    invalidIDs = []
    for item in input:
        if "-" in item:
            items = item.split("-")
            start = int(items[0])
            end = int(items[1])
            for i in range(start, end+1):
                if isInvalidID(str(i), patt):
                    invalidIDs.append(i)
        else:
            if isInvalidID(item, patt):
                invalidIDs.append(int(item))

    return sum(invalidIDs)

def getPart1(input) -> int:
    return getInvalidSum(input)

def getPart2(input) -> int:
    return getInvalidSum(input, r"^(.+)\1+$")

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split(",")
    answer = [0,0] #part1, part2

    answer[0] = getPart1(input)
    answer[1] = getPart2(input)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
