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
    if not os.getcwd().endswith('2025'): os.chdir('2025')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2025'): os.chdir('2025')
    f = open(path, 'w')
    f.write(s)
    f.close()

def getAdjacentSpotValues(floor_map : list, x : int, y : int) -> list:
    spots = []
    maxPos = [len(floor_map)-1, len(floor_map[x])-1]
    if y > 0: spots.append(floor_map[x][y-1])
    if y < maxPos[1]: spots.append(floor_map[x][y+1])
    if x > 0: spots.append(floor_map[x-1][y])
    if x < maxPos[0]: spots.append(floor_map[x+1][y])
    if x > 0 and y > 0: spots.append(floor_map[x-1][y-1])
    if x > 0 and y < maxPos[1]: spots.append(floor_map[x-1][y+1])
    if x < maxPos[0] and y > 0: spots.append(floor_map[x+1][y-1])
    if x < maxPos[0] and y < maxPos[1]: spots.append(floor_map[x+1][y+1])
    return spots

def canBeRemoved(floor_map : list, x : int, y : int) -> bool:
    spots = getAdjacentSpotValues(floor_map, x, y)
    numAdj = 0
    for s in spots:
        if s == "@": numAdj += 1
    return numAdj < 4

def getPart1(floor_map : list) -> int:
    numRolls = 0
    for y in range(len(floor_map[0])):
        for x in range(len(floor_map)):
            if floor_map[x][y] == "@":
                if canBeRemoved(floor_map, x, y): numRolls += 1
    return numRolls

def getPart2(floor_map : list) -> int:
    numRemoved = 0
    
    while True:
        toBeRemoved = []
        for y in range(len(floor_map[0])):
            for x in range(len(floor_map)):
                if floor_map[x][y] == "@":
                    if canBeRemoved(floor_map, x, y): toBeRemoved.append((x, y))
        numRemoved += len(toBeRemoved)
        for x,y in toBeRemoved:
            floor_map[x][y] = "."
        if len(toBeRemoved) == 0: break
    return numRemoved

def getAnswer(input, isSample) -> list:
    floor_map = [list(line) for line in input.replace("\r", "").split("\n")]
    answer = [0,0] #part1, part2


    answer[0] = getPart1(floor_map)
    answer[1] = getPart2(floor_map)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
