import os
import sys
import copy

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

moveValues = {"^":(0,-1), ">":(1,0), "v":(0,1), "<":(-1,0)} # (x, y) / (col, row)
moves = ["^", ">", "v", "<"] # in order

def findGuard(board : list) -> tuple:
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] in moves:
                return (c, r)

def addTuples(t1 : tuple, t2 : tuple) -> tuple:
    return (t1[0] + t2[0], t1[1] + t2[1])

def rotateGuard(board : list, currPos : tuple) -> None:
    index = moves.index(board[currPos[1]][currPos[0]]) + 1
    if index >= len(moves):
        index = 0
    board[currPos[1]][currPos[0]] = moves[index]
    
def tryMoveGuard(board : list, currPos : tuple) -> tuple:
    currGuard = board[currPos[1]][currPos[0]]
    moveVal = moveValues[currGuard]
    nextPos = addTuples(currPos, moveVal)
    if nextPos[0] < 0 or nextPos[0] >= len(board[0]) or nextPos[1] < 0 or nextPos[1] >= len(board):
        board[currPos[1]][currPos[0]] = "X"
        return nextPos
    
    if board[nextPos[1]][nextPos[0]] == "#":
        rotateGuard(board, currPos)
        return currPos
    else:
        board[currPos[1]][currPos[0]] = "X"
        board[nextPos[1]][nextPos[0]] = currGuard
        return nextPos

def countSpaces(board) -> int:
    sum = 0
    for r in board:
        for c in r:
            if c == "X": sum += 1
    return sum
    
def pathIsLoop(path : list) -> bool:
    last = path[-1]
    for m in range(len(path)-1):
        if m == last:
            return True
    return False

def getPart1(board : list, moveMem : list) -> int:
    currPos = findGuard(board)
    currDir = board[currPos[1]][currPos[0]]
    #moveMem = [(currDir, currPos)]
    while currPos[0] >= 0 and currPos[0] < len(board[0]) and currPos[1] >= 0 and currPos[1] < len(board):
        currDir = board[currPos[1]][currPos[0]]
        moveMem.append((currDir, currPos))
        # save currDir/moveMem from previous in case next move goes off the board
        currPos = tryMoveGuard(board, currPos)
        
    return countSpaces(board)

def getPart2(input : list, moveMemP1 : list) -> int:
    count = 0
    start = moveMemP1[0]
    for p in range(1, len(moveMemP1)):
        board = copy.deepcopy(input)
        loc = moveMemP1[p][1]
        if loc[0] == start[1][0] and loc[1] == start[1][1]:
            #print("same")
            continue
        board[loc[1]][loc[0]] = "#"
        print(f"start = {start}, setting board[{loc[1]}][{loc[0]}] = '#'")
        currDir, currPos = start
        pathMem = []#[start]
        while currPos[0] >= 0 and currPos[0] < len(board[0]) and currPos[1] >= 0 and currPos[1] < len(board):
            currDir = board[currPos[1]][currPos[0]]
            pathMem.append((currDir, currPos))
            if len(pathMem) > 1 and pathIsLoop(pathMem):
                count += 1
                print(count)
                break
            
            print(f"trying to move guard from {currPos}")
            currPos = tryMoveGuard(board, currPos)
            

    return count

def getAnswer(input, isSample) -> list:
    input = [list(x) for x in input.replace("\r", "").split("\n")]
    answer = [0,0] #part1, part2

    moveMemP1 = []
    answer[0] = getPart1(copy.deepcopy(input), moveMemP1)
    answer[1] = getPart2(copy.deepcopy(input), moveMemP1)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
