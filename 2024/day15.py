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

MoveDict = {"<":(0,-1),">":(0,1),"^":(-1,0),"v":(1,0)}

def addTupleToPosInPlace(pos : list, _tuple : tuple) -> None:
    pos[0] += _tuple[0]
    pos[1] += _tuple[1]

def addTupleToPos(pos : list, _tuple : tuple) -> list:
    return [pos[0] + _tuple[0], pos[1] + _tuple[1]]

def posInBounds(_map : list, _pos : list) -> bool:
    if _pos[0] < 0 or _pos[0] >= len(_map) or _pos[1] < 0 or _pos[1] >= len(_map[0]): return False
    return True

def getMapItemFromPos(_map : list, _pos : list) -> str:
    if _pos[0] < 0 or _pos[0] >= len(_map) or _pos[1] < 0 or _pos[1] >= len(_map[0]): return "#"
    return _map[_pos[0]][_pos[1]]

def setMapItem(_map : list, _pos : list, _item : str):
    if posInBounds(_map, _pos):
        _map[_pos[0]][_pos[1]] = _item
        
def printMap(_map : list) -> None:
    for r in range(len(_map)):
        row = ""
        for c in range(len(_map[0])):
            row += _map[r][c]
        print(row)

def getRobotPos(_map : list) -> list:
    for r in range(1,len(_map)-1):
        for c in range(1, len(_map[0])-1):
            if _map[r][c] == "@":
                return [r, c]
            
def tryMove(_robot : list, _map : list, _move : tuple) -> bool:
    currPos = _robot

    moveList = []
    while (item := getMapItemFromPos(_map, (currPos := addTupleToPos(currPos, _move)))) != "#":
        if item == ".":
            moveList.append(_robot)
            break
        moveList.append(currPos) # add item to move list
        
    if len(moveList) > 0:
        for i in range(len(moveList)):
            moveTo = addTupleToPos(moveList[i], _move)
            if getMapItemFromPos(_map, moveTo) == "#":
                return False
            setMapItem(_map, moveTo, getMapItemFromPos(_map, moveList[i]))
        setMapItem(_map, _robot, ".")
        return True
    return False # didn't move

def calcCoord(_box : tuple) -> int:
    return _box[0] * 100 + _box[1]

def getPart1(_map : list, _moves : str) -> int:
    for r in range(len(_map)):
        _map[r] = list(_map[r]) # change strings to lists so they can be modified in place

    robot = getRobotPos(_map)
    for m in _moves:
        print(f"Move: {m}")
        if tryMove(robot, _map, MoveDict[m]):
            robot = addTupleToPos(robot, MoveDict[m])
    
    sum = 0
    for r in range(1, len(_map)):
        for c in range(1, len(_map[0])):
            if _map[r][c] == "O":
                sum += calcCoord((r, c))
    return sum

def resizeMap(input : list) -> list:
    newMap = []
    for r in input:
        row = ""
        for c in r:
            match c:
                case "#":
                    row += "##"
                case ".":
                    row += ".."
                case "O":
                    row += "[]"
                case "@":
                    row += "@."
        newMap.append(list(row))
    return newMap
            
def getPart2(input : list, _moves : str) -> int:
    _map = resizeMap(input)
    
    robot = getRobotPos(_map)
    # for m in _moves:
    #     print(f"Move: {m}")
    #     if tryMove(robot, _map, MoveDict[m]):
    #         robot = addTupleToPos(robot, MoveDict[m])
    
    sum = 0
    for r in range(1, len(_map)):
        for c in range(1, len(_map[0])):
            if _map[r][c] == "[":
                sum += calcCoord((r, c))
    return sum

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n\n")
    answer = [0,0] #part1, part2

    m = input[0].split("\n")
    moves = input[1].replace("\n", "")

    #answer[0] = getPart1(m, moves)
    answer[1] = getPart2(input[0].split("\n"), moves)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
