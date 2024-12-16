import os
import sys

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

def printList(_list : list) -> None:
    for r in _list:
        print(r)

def rotateMatrix45(_list : list) -> list:
    newList = []
    for r in range(len(_list)-1, -len(_list[0]), -1):
        newItem = ""
        for c in range(len(_list[0])):
            if r+c >= 0 and r+c < len(_list):
                newItem += _list[r+c][c]
        if len(newItem) > 0: newList.append(newItem)

    return newList

def rotateMatrix270(_list : list) -> list:
    newList = []
    for r in range(len(_list)+len(_list[0])-1):
        newItem = ""
        for c in range(len(_list[0])):
            if r-c >= 0 and r-c < len(_list):
                newItem += _list[r-c][c]
        if len(newItem) > 0: newList.append(newItem)

    return newList

def rotateMatrix90(_list : list) -> list:
    newList = []
    for c in range(len(_list[0])):
        newRow = ""
        for r in range(len(_list)):
            newRow += _list[r][c]
        newList.append(newRow)
    return newList

def buildList(input : list) -> list:
    xmas = input.copy()
    xmas += rotateMatrix90(input) #vertical
    xmas += rotateMatrix45(input) #diag left to right
    xmas += rotateMatrix270(input) #diag right to left
    
    newList = []
    for r in xmas:
        if len(r) >= 4:
            newList.append(r)
            newList.append(r[::-1])
    
    return newList

def getPart1(input : list) -> int:
    xmas = buildList(input)
    printList(xmas)
    x : str
    sum = 0
    for x in xmas:
        sum += x.count("XMAS")
    return sum

def isXMAS(input : list, pos : tuple) -> bool:
    if input[pos[1]][pos[0]] != "A": return False
    upLeft = input[pos[1]-1][pos[0]-1]
    downRight = input[pos[1]+1][pos[0]+1]
    upRight = input[pos[1]-1][pos[0]+1]
    downLeft = input[pos[1]+1][pos[0]-1]
    if (upLeft == "M" and downRight == "S") or (upLeft == "S" and downRight == "M"):
        if (upRight == "M" and downLeft == "S") or (upRight == "S" and downLeft == "M"):
            return True
    return False

def getPart2(input : list) -> int:
    count = 0
    for r in range(1, len(input)-1):
        for c in range(1, len(input[0])-1):
            if isXMAS(input, (c, r)):
                count += 1
    return count

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2


    answer[0] = getPart1(input)
    answer[1] = getPart2(input)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
