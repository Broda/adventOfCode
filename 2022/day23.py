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
    if not os.getcwd().endswith('2022'): os.chdir('2022')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2022'): os.chdir('2022')
    f = open(path, 'w')
    f.write(s)
    f.close()

def tupleAdd(t1, t2):
    return (t1[0]+t2[0],t1[1]+t2[1])

class Elf:
    def __init__(self, loc) -> None:
        self.loc = loc
        self.directions = ['N','S','W','E'] # initial order
        self.updateNeighbors()
    
    def updateNeighbors(self) -> None:
        self.neighbors = []
        for y in range(self.loc[1]-1,self.loc[1]+2):
            for x in range(self.loc[0]-1, self.loc[0]+2):
                if self.loc != (x,y):
                    self.neighbors.append((x,y))

    def updateDirection(self) -> None:
        self.directions.append(self.directions.pop(0))

    def move(self, pos) -> None:
        self.loc = pos
        self.updateNeighbors()

    def tryMove(self, grid) -> tuple:
        stay = True
        for n in self.neighbors:
            if n in grid.keys():
                stay = False
                break
        
        if stay: return self.loc

        move = self.loc

        for d in self.directions:
            match d:
                case 'N':
                    pos = tupleAdd(self.loc, (0,-1))
                    if pos in grid.keys(): continue
                    pos = tupleAdd(self.loc, (-1,-1))
                    if pos in grid.keys(): continue
                    pos = tupleAdd(self.loc, (1,-1))
                    if pos in grid.keys(): continue
                    return tupleAdd(self.loc, (0,-1))
                case 'S':
                    pos = tupleAdd(self.loc, (0,1))
                    if pos in grid.keys(): continue
                    pos = tupleAdd(self.loc, (-1,1))
                    if pos in grid.keys(): continue
                    pos = tupleAdd(self.loc, (1,1))
                    if pos in grid.keys(): continue
                    return tupleAdd(self.loc, (0,1))
                case 'W':
                    pos = tupleAdd(self.loc, (-1,0))
                    if pos in grid.keys(): continue
                    pos = tupleAdd(self.loc, (-1,-1))
                    if pos in grid.keys(): continue
                    pos = tupleAdd(self.loc, (-1,1))
                    if pos in grid.keys(): continue
                    return tupleAdd(self.loc, (-1,0))
                case 'E':
                    pos = tupleAdd(self.loc, (1,0))
                    if pos in grid.keys(): continue
                    pos = tupleAdd(self.loc, (1,-1))
                    if pos in grid.keys(): continue
                    pos = tupleAdd(self.loc, (1,1))
                    if pos in grid.keys(): continue
                    return tupleAdd(self.loc, (1,0))
                case _:
                    return move
        return move
    
def buildGrid(input) -> tuple[dict, list, list]:
    grid = {}
    x_bounds = [sys.maxsize, -sys.maxsize]
    y_bounds = [sys.maxsize, -sys.maxsize]
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == '#':
                grid[(x,y)] = Elf((x,y))
                x_bounds[0] = min(x_bounds[0], x)
                x_bounds[1] = max(x_bounds[1], x)
                y_bounds[0] = min(y_bounds[0], y)
                y_bounds[1] = max(y_bounds[1], y)

    return grid, x_bounds, y_bounds

def countEmptySpots(grid, x_bounds, y_bounds) -> int:
    count = 0
    for x in range(x_bounds[0], x_bounds[1]+1):
        for y in range(y_bounds[0], y_bounds[1]+1):
            if (x, y) not in grid.keys(): count += 1
    return count

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    elves, x_bounds, y_bounds = buildGrid(input)

    round = 1
    while True:
        # step 1: move proposals
        proposed_pos = {}
        for k, e in elves.items():
            newPos = e.tryMove(elves)
            if newPos in proposed_pos.keys():
                proposed_pos[newPos].append(k)
            else:
                proposed_pos[newPos] = [k]
        
        # step 2: move only elves that can
        moveCount = 0
        for k, p in proposed_pos.items():
            if len(p) == 1 and p[0] != k:
                moveCount += 1
                elves[p[0]].move(k)
                elves[k] = elves.pop(p[0])
                x_bounds[0] = min(x_bounds[0], k[0])
                x_bounds[1] = max(x_bounds[1], k[0])
                y_bounds[0] = min(y_bounds[0], k[1])
                y_bounds[1] = max(y_bounds[1], k[1])
        
        if moveCount == 0: break

        # step 3: update direction decisions
        for k, e in elves.items():
            e.updateNeighbors()
            e.updateDirection()

        round += 1

    answer[0] = countEmptySpots(elves, x_bounds, y_bounds)
    answer[1] = round
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))



