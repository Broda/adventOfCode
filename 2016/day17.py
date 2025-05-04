import os
import sys
import hashlib

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
    if not os.getcwd().endswith('2016'): os.chdir('2016')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2016'): os.chdir('2016')
    f = open(path, 'w')
    f.write(s)
    f.close()

def getHash(path : str) -> str:
    return hashlib.md5(path.encode('utf-8')).hexdigest()

def getOpenNeighbors(path : str, loc : tuple) -> list:
    h = getHash(path)
    x, y = loc
    possible = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)] #up, down, left, right
    neighbors = []
    for i in range(4):
        if h[i] in "bcdef": #open
            n = possible[i]
            if n[0] >= 0 and n[1] >= 0 and n[0] < 4 and n[1] < 4:
                neighbors.append(n)
    return neighbors

def getPart1(input : list) -> list:
    answers = []
    
    return answers

def getPart2() -> int:
    return 0

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2


    answer[0] = getPart1()
    answer[1] = getPart2()
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
