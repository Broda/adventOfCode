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

MoveDict = {"<":(-1,0),">":(1,0),"^":(0,-1),"v":(0,1)}

def addTupleToPosInPlace(pos : list, _tuple : tuple) -> None:
    pos[0] += _tuple[0]
    pos[1] += _tuple[1]

def addTupleToPos(pos : list, _tuple : tuple) -> list:
    return [pos[0] + _tuple[0], pos[1] + _tuple[1]]

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
                return [c, r] # positions are [x, y]
            
def tryMove(_robot : list, _map : list, _move : tuple) -> bool:
    startPos = _robot

    while True:
        nextSpotPos = addTupleToPos(_robot, _move)
        nextSpot = _map[nextSpotPos[1]][nextSpotPos[0]]
        if nextSpot != "O":
            break
    
    if nextSpot == "#":
        return False

    # nextSpot must be a .
    revMove = (-1 * _move[0], -1 * _move[1])
    while True:
        _map[nextSpotPos[1]][nextSpotPos[0]] = _map[nextSpotPos[1] + revMove[1]][nextSpotPos[0] + revMove[0]]
        if _map[nextSpotPos[1]][nextSpotPos[0]] == "@":
            _robot = nextSpotPos
        addTupleToPosInPlace(nextSpotPos, revMove)
        if nextSpotPos[0] == startPos[0] and nextSpotPos[1] == startPos[1]:
            _map[nextSpotPos[1]][nextSpotPos[0]] = "."
            break

    return True

def calcCoord(_box : tuple) -> int:
    return _box[1] * 100 + _box[0]

def getPart1(_map : list, _moves : str) -> int:
    for r in range(len(_map)):
        _map[r] = list(_map[r]) # change strings to lists so they can be modified in place

    printMap(_map)
    robot = getRobotPos(_map)
    for m in _moves:
        print(f"Move: {m}")
        tryMove(robot, _map, MoveDict[m])
        printMap(_map)
    
    sum = 0
    for r in range(1, len(_map)):
        for c in range(1, len(_map[0])):
            if _map[r][c] == "O":
                sum += calcCoord((c, r))
    return sum

def getPart2() -> int:
    return 0

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n\n")
    answer = [0,0] #part1, part2

    m = input[0].split("\n")
    moves = input[1].replace("\n", "")

    answer[0] = getPart1(m, moves)
    answer[1] = getPart2()
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
