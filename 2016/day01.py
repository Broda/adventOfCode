import os
import sys
import numpy as np

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

def getDirection(curr : tuple, turn : str) -> tuple:
    directions : tuple = ((0,1),(1,0),(0,-1),(-1,0))
    index = directions.index(curr)
    if turn == "R":
        index += 1
    else:
        index -= 1
    if index == 4: index = 0
    if index == -1: index = 3
    return directions[index]

def addLists(A : list, B : list) -> list:
    return [A[0] + B[0], A[1] + B[1]]

def move(currPos : list, currDir : tuple, turn : str, amt : int) -> list:
    newDir = getDirection(currDir, turn)
    moveVect = [newDir[0] * amt, newDir[1] * amt]
    newPos = (np.array(currPos) + np.array(moveVect)).tolist()
    return newPos, newDir

def getPart1(input : list) -> int:
    dir = (0,-1)
    currPos = [0,0]

    for inp in input:
        currPos, dir = move(currPos, dir, inp[0:1], int(inp[1:]))
        
    dist = abs(currPos[0]) + abs(currPos[1])

    return dist

def getPart2(input : list) -> int:
    dir = (0,1)
    currPos = [0,0]
    positions = [currPos.copy()]

    for inp in input:
        dir = getDirection(dir, inp[0:1])
        for m in range(int(inp[1:])):
            currPos = addLists(currPos, list(dir))        
            if currPos in positions:
                print(f'{currPos} in positions, return distance')
                return abs(currPos[0]) + abs(currPos[1])
            positions.append(currPos.copy())
    
    return 0

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")[0]
    answer = [0,0] #part1, part2

    answer[0] = getPart1(input.split(", "))
    answer[1] = getPart2(input.split(", "))
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
