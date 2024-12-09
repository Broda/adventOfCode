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
    if not os.getcwd().endswith('2024'): os.chdir('2024')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2024'): os.chdir('2024')
    f = open(path, 'w')
    f.write(s)
    f.close()

def getPart1(input) -> int:
    sum = 0
    matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", input)
    m : str
    for m in matches:
        mul = m.replace("mul(", "").replace(")", "").split(",")
        sum += int(mul[0]) * int(mul[1])
    return sum

def getPart2(input) -> int:
    sum = 0
    en = True
    matches = re.findall(r"(mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\))", input)
    m : str
    for m in matches:
        if m.startswith("mul") and en:
            mul = m.replace("mul(", "").replace(")", "").split(",")
            sum += int(mul[0]) * int(mul[1])
        elif m.startswith("don"):
            en = False
        elif m.startswith("do"):
            en = True
    return sum

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2


    answer[0] = getPart1(''.join(input))
    answer[1] = getPart2(''.join(input))
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
