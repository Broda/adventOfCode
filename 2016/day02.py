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
    if not os.getcwd().endswith('2016'): os.chdir('2016')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2016'): os.chdir('2016')
    f = open(path, 'w')
    f.write(s)
    f.close()

def getKeyCoord(keypad : tuple, key : int) -> tuple:
    for y in range(len(keypad)):
        for x in range(len(keypad[0])):
            if keypad[y][x] == key: return (x, y)

def getKeyAtPos(keypad : tuple, pos : list) -> int:
    return keypad[pos[1]][pos[0]]

def addTupleToList(A : list, T : tuple) -> list:
    return [A[0] + T[0], A[1] + T[1]]

def posOutOfBounds(keypad : tuple, pos : list) -> bool:
    if pos[0] < 0 or pos[0] >= len(keypad[0]) or pos[1] < 0 or pos[1] >= len(keypad):
        return True
    key = getKeyAtPos(keypad, pos)
    if key == 0: return True
    return False

def getNextKey(keypad : tuple, currKey : int, path : str) -> int:
    directions = {"U":(0,-1), "D":(0,1), "L":(-1,0), "R":(1,0)}
    currPos = getKeyCoord(keypad, currKey)
    for step in list(path):
        dir = directions[step]
        tempPos = addTupleToList(currPos, dir)
        if not posOutOfBounds(keypad, tempPos):
            currPos = tempPos
    return getKeyAtPos(keypad, currPos)

def getPart1(input : list) -> str:
    keypad = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    currKey = 5
    keys = ""

    for line in input:
        currKey = getNextKey(keypad, currKey, line)
        keys += str(currKey)

    return keys

def getPart2(input : list) -> str:
    keypad = ((0, 0, 1, 0, 0), (0, 2, 3, 4, 0), (5, 6, 7, 8, 9), (0, 10, 11, 12, 0), (0, 0, 13, 0, 0))
    currKey = 5
    keys = ""

    for line in input:
        currKey = getNextKey(keypad, currKey, line)
        letters = {10: "A", 11: "B", 12: "C", 13: "D"}
        if currKey > 9:
            keys += letters[currKey]
        else:
            keys += str(currKey)

    return keys

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    answer[0] = getPart1(input)
    answer[1] = getPart2(input)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
