import os
import sys
import re

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
    return f.read()

def writeFile(path, s):
    if not os.getcwd().endswith('2022'): os.chdir('2022')
    f = open(path, 'w')
    f.write(s)
    f.close()

def buildGrid(input):
    grid = input
    max_len = -sys.maxsize
    start = None
    for y in range(len(input)):
        max_len = max(max_len, len(input[y]))
    max_len += 1

    grid.insert(0, ' '*max_len)
    for y in range(1, len(grid)):
        grid[y] = ' ' + grid[y]
        if len(input[y]) < max_len:
            grid[y] += ' '*(max_len - len(input[y]))
        for x in range(len(grid[y])):
            if grid[y][x] == '.' and start is None:
                start = (x,y)
    return grid, start

FACINGS = [(1,0), (0,1), (-1,0), (0,-1)]
TURNS = {'R':1,'L':-1}

def tupleAdd(t1, t2):
    return (t1[0]+t2[0],t1[1]+t2[1])

def tupleSub(t1, t2):
    return (t1[0]-t2[0],t1[1]-t2[1])

def getBoundsOfRow(grid, row):
    bounds = [None, None]
    for x in range(len(grid[row])):
        if grid[row][x] == ' ':
            if bounds[0] is None: continue
            if bounds[1] is None: 
                bounds[1] = x-1
                return bounds
        else:
            if bounds[0] is None:
                bounds[0] = x
    if bounds[1] is None: bounds[1] = len(grid[row])-1
    return bounds

def getBoundsOfCol(grid, col):
    bounds = [None,None]
    for y in range(len(grid)):
        if grid[y][col] == ' ':
            if bounds[0] is None: continue
            if bounds[1] is None:
                bounds[1] = y-1
                return bounds
        elif bounds[0] is None:
            bounds[0] = y
    
    if bounds[1] is None: bounds[1] = len(grid)-1
    return bounds

def tryMove(grid, loc, facing):
    # trying to move 1 space
    x_bounds = getBoundsOfRow(grid, loc[1])
    y_bounds = getBoundsOfCol(grid, loc[0])
    
    newLoc = tupleAdd(loc, FACINGS[facing])
    
    s = '\ttryMove {} {} => {}\n'.format(loc, FACINGS[facing], newLoc)
    if newLoc[0] > x_bounds[1]: newLoc = (x_bounds[0],newLoc[1])
    if newLoc[0] < x_bounds[0]: newLoc = (x_bounds[1],newLoc[1])
    if newLoc[1] > y_bounds[1]: 
        s += 'y_bounds[0] for col {} is {}\n'.format(loc[0], y_bounds[0])
        newLoc = (newLoc[0], y_bounds[0])
    if newLoc[1] < y_bounds[0]: 
        s += 'y_bounds[1] for col {} is {}\n'.format(loc[0], y_bounds[1])
        newLoc = (newLoc[0],y_bounds[1])
    
    s += '\t\tgrid[{}] = "{}"\n'.format(newLoc, grid[newLoc[1]][newLoc[0]])

    if grid[newLoc[1]][newLoc[0]] == '.': return newLoc, s
    return loc, s

def onBoundary(loc, dir):
    x, y = loc
    xd, yd = dir

    if x % 50 == 1 and xd < 0: return True
    if x % 50 == 0 and xd > 0: return True
    if y % 50 == 1 and yd < 0: return True
    if y % 50 == 0 and yd > 0: return True
    return False 

def getDestination(loc, dir):
    x, y = loc
    xd, yd = dir

    if yd < 0: # UP
        if y == 1:
            if x in range(51,101): # A.top -> F.left
                return (1, x + 100), (1, 0) # right
            elif x in range(101,151): # B.top -> F.bottom
                return (x - 100, 200), dir
        if y == 51:
            if x in range(51,101): # C.top -> A.bottom
                return (x, y - 1), dir
        if y == 101:
            if x in range(51,101): # D.top -> C.bottom
                return (x, y - 1), dir
            elif x in range(1, 51): # E.top -> C.left
                return (51, x + 50), (1, 0) # face right
        if y == 151:
            if x in range(1,51): # F.top -> E.bottom
                return (x, y - 1), dir
    if yd > 0: # DOWN
        if y == 50:
            if x in range(51, 101): # A.bottom -> C.top
                return (x, y + 1), dir
            elif x in range(101, 151): # B.bottom -> C.right
                return (100, x - y), (-1,0) # left
        if y == 100:
            if x in range(51, 101): # C.bottom -> D.top
                return (x, y + 1), dir
        if y == 150:
            if x in range(51, 101): # D.bottom -> F.right
                return (50, x + 100), (-1, 0) # left
            elif x in range(1, 51): # E.bottom -> F.top
                return (x, y + 1), dir
        if y == 200:
            if x in range(1,51): # F.bottom -> B.top
                return (x + 100, 1), dir
    if xd < 0: # LEFT
        if x == 1:
            if y in range(101, 151): # E.left -> A.left_flip
                return (51, 151 - y), (1, 0) # right
            elif y in range(151, 201): # F.left -> A.top
                return (y - 100, 1), (0, 1) # down
        if x == 51:
            if y in range(1, 51): # A.left -> E.left_flip
                return (1, 151 - y), (1,0) # right
            elif y in range(51,101): # C.left -> E.top
                return (y - 50, 101), (0,1) # down
            elif y in range(101, 151): # D.left -> E.right
                return (x - 1, y), dir
        if x == 101:
            if y in range(1, 51): # B.left -> A.right
                return (x - 1, y), dir
    if xd > 0: # RIGHT
        if x == 50:
            if y in range(101, 151): # E.right -> D.left
                return (x + 1, y), dir # right
            elif y in range(151, 201): # F.right -> D.bottom
                return (y - 100, 150), (0, -1) # up
        if x == 100:
            if y in range(1, 51): # A.right -> B.left 
                return (x + 1, y), dir
            elif y in range(51, 101): # C.right -> B.bottom
                return (y + 50, 50), (0, -1) # up
            elif y in range(101, 151): # D.right -> B.right_flip
                return (150, 151 - y), (-1, 0) # left
        if x == 150:
            if y in range(1, 51): # B.right -> D.right_flip
                return (100, 151 - y), (-1, 0) # left
    return loc, dir
    
# A
#- row 1 col 51-100, up -> F.left (51,1) => (1,151), (100,1) => (1,200), face => right
#- row 50 col 51-100, down -> C.top (51,50) => (51,51), (100,50) => (100,51), face => down
#- row 1-50 col 51, left -> E.left_flip (51,1) => (1,150), (51,50) => (1,101), face => right
#- row 1-50 col 100, right -> B.left (100,1) => (101,1), (100,50) => (101,50), face => right

# B
#- row 1 col 101-150, up -> F.bottom (101,1) => (1,200), (150,1) => (50,200) , face => up
#- row 50 col 101-150, down -> C.right (101,50) => (100,51), (150,50) => (100,100), face => left
#- row 1-50 col 101, left -> A.right (101,1) => (100,1), (101,50) => (100,50), face => left
#- row 1-50 col 150, right -> D.right_flip (150,1) => (100,150), (150,50) => (100,101), face => left

# C
#- row 51 col 51-100, up -> A.bottom (51,51) => (51,50), (100,51) => (100,50), face => up
#- row 100 col 51-100, down -> D.top (51,100) => (51,101), (100,100) => (100,101), face => down
#- row 51-100 col 51, left -> E.top (51,51) => (1,101), (51,100) => (50,101), face => down
#- row 51-100 col 100, right -> B.bottom (100,51) => (101,50), (100,100) => (150,50), face => up

# D
#- row 101 col 51-100, up -> C.bottom (51,101) => (51,100), (100,101) => (100,100), face => up
#- row 150 col 51-100, down -> F.right (51,150) => (50,51), (100,150) => (50,200), face => left
#- row 101-150 col 51, left -> E.right (51,101) => (50,101), (51,150) => (50,150), face => left
#- row 101-150 col 100, right -> B.right_flip (100,101) => (150,50), (100,150) => (150,1), face => left

# E
#- row 101 col 1-50, up -> C.left (1,101) => (51,51), (50,101) => (51,100), face => right
#- row 150, col 1-50, down -> F.top (1,150) => (1,151), (50,150) => (50,151), face => down
#- row 101-150 col 1, left -> A.left_flip (1,101) => (51,50), (1,150) => (51,1), face => right
#- row 101-150 col 50, right -> D.left (50,101) => (51,101), (50,150) => (51,150), face => right

# F
#- row 151, col 1-50, up -> E.bottom (1,151) => (1,150), (50,151) => (50,150), face => up
#- row 200 col 1-50, down -> B.top (1,200) => (101,1), (50,200) => (150,1), face => down
#- row 151-200 col 1, left -> A.top (1,151) => (51,1), (1,200) => (100,1), face => down
#- row 151-200 col 50, right -> D.bottom (50,151) => (51,150), (50,200) => (100,150), face => up


def tryMove2(grid, loc, facing):
    newFacing = facing
    s = '\ttryMove2 {} {} {} => '.format(loc, facing, FACINGS[facing])
    if onBoundary(loc, FACINGS[facing]):
        newLoc, newFacing = getDestination(loc, FACINGS[facing])
        newFacing = FACINGS.index(newFacing)
    else:
        newLoc = tupleAdd(loc, FACINGS[facing])
    
    s += '{} {} {}\n'.format(newLoc, newFacing, FACINGS[newFacing])

    s += '\t\tgrid[{}] = "{}"'.format(newLoc, grid[newLoc[1]][newLoc[0]])

    if grid[newLoc[1]][newLoc[0]] == '.': return newLoc, newFacing, s
    return loc, facing, s

def printGrid(grid):
    for y in range(len(grid)):
        print('"{}"'.format(grid[y]))

def getPart1(grid, start, facing, path):
    s = ''
    loc = start
    for p in path:
        s += 'Loc: {}, Facing: {} {}, Path: {}\n'.format(loc, facing, FACINGS[facing], p)
        if type(p) is int:
            for _ in range(p):
                newLoc, debugStr = tryMove(grid, loc, facing)
                s += debugStr
                if newLoc == loc: break
                loc = newLoc
        elif p in ['R','L']:
            facing += TURNS[p]
            if facing >= len(FACINGS): facing = 0
            if facing < 0: facing = len(FACINGS)-1
        s+= '=> New Loc: {}, New Facing: {} {}\n'.format(loc, facing, FACINGS[facing])

    writeFile('day22debug_part1.txt', s)

    return loc[1] * 1000 + loc[0] * 4 + facing

def getPart2(grid, start, facing, path):
    s = ''
    loc = start
    for p in path:
        s += 'Loc: {}, Facing: {} {}, Path: {}\n'.format(loc, facing, FACINGS[facing], p)
        if type(p) is int:
            for _ in range(p):
                newLoc, facing, debugStr = tryMove2(grid, loc, facing)
                s += debugStr
                if newLoc == loc: break
                loc = newLoc
        elif p in ['R','L']:
            facing += TURNS[p]
            if facing >= len(FACINGS): facing = 0
            if facing < 0: facing = len(FACINGS)-1
        s+= '=> New Loc: {}, New Facing: {} {}\n'.format(loc, facing, FACINGS[facing])

    writeFile('day22debug_part2.txt', s)

    return loc[1] * 1000 + loc[0] * 4 + facing

def getAnswer(input, isSample):
    input = input.replace("\r", "").split("\n\n")
    answer = [0,0] #part1, part2

    grid, start = buildGrid(input[0].split('\n'))
    path = re.findall("(\d+|[RL])", input[1])
    path = [int(value) if value.isnumeric() else value for value in path]

    facing = 0
    answer[0] = getPart1(grid, start, facing, path)
    
    facing = 0
    answer[1] = getPart2(grid, start, facing, path)

    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))



