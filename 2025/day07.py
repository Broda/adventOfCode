import os
import sys
from collections import defaultdict

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

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    start = input[0].index("S")
    splitters = 0
    tachs = defaultdict(int)
    tachs[start] = 1
    for line in input[::2]:
        for i in tuple(tachs.keys()):
            if line[i] == "^":
                splitters += 1
                tachs[i-1] += tachs[i]
                tachs[i+1] += tachs[i]
                del tachs[i]

    return [splitters, sum(tachs.values())]

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
