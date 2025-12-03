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
            return readFile(samplePath)
        case "2":
            return readFile(inputPath)
        case "3":
            return readFile(input("File Name: "))
        case "4":
            return input("Input: ")
        case _:
            print("Invalid option. Try Again.\n")
            return menu()

def readFile(path):
    if not os.getcwd().endswith('2022'): os.chdir('2022')
    f = open(path, "r")
    return f.read().strip()

AIR = 0
ROCK = 1
SAND = 2
SAND_START = 3
grid_str = {AIR:'.',ROCK:'#',SAND:'o',SAND_START:'+'}

def buildGrid(input):
    grid = {}
    grid[(500,0)] = SAND_START
    grid_start = [500,0]
    grid_stop = [0,0]

    for l in input:
        coords = list(map(lambda c: eval(c), l.split(' -> ')))
        for i in range(len(coords)):
            grid_start[0] = min(grid_start[0],coords[i][0])
            grid_start[1] = min(grid_start[1],coords[i][1])
            grid_stop[0] = max(grid_stop[0],coords[i][0])
            grid_stop[1] = max(grid_stop[1],coords[i][1])

            #print(coords, grid_start, grid_stop)

            grid[coords[i]] = ROCK
            if i+1 >= len(coords): break
            grid_start[0] = min(grid_start[0],coords[i+1][0])
            grid_start[1] = min(grid_start[1],coords[i+1][1])
            grid_stop[0] = max(grid_stop[0],coords[i+1][0])
            grid_stop[1] = max(grid_stop[1],coords[i+1][1])

            x_min = min(coords[i][0], coords[i+1][0])
            x_max = max(coords[i][0], coords[i+1][0])
            y_min = min(coords[i][1], coords[i+1][1])
            y_max = max(coords[i][1], coords[i+1][1])
            for x in range(x_min, x_max+1):
                for y in range(y_min, y_max+1):
                    grid[(x,y)] = ROCK

    for y in range(grid_start[1], grid_stop[1]+1):
        for x in range(grid_start[0], grid_stop[0]+1):
            if (x, y) not in grid.keys():
                grid[(x,y)] = AIR

    return grid, grid_start, grid_stop
    
def part2Grid(grid, start, stop):
    
    for y in range(stop[1]+1, stop[1]+2):
        for x in range(start[0],stop[0]+1):
            # print('adding ({},{})'.format(x, y))
            grid[(x, y)] = AIR
    stop[1] += 1

    
    return grid, start, stop

def printGrid(grid, start, stop):
    print_grid_str = ''
    for y in range(start[1],stop[1]+1):
        r = ''
        for x in range(start[0], stop[0]+1):
            r += grid_str[grid[(x,y)]]

        print_grid_str += r + '\n'

    print(print_grid_str)

def addColumn(grid, x, start, stop):
    start[0] = min(x, start[0])
    stop[0] = max(x, stop[0])
    for y in range(start[1], stop[1]+1):
        grid[(x, y)] = AIR
        
    return grid, start, stop

def generateSand(grid, start, stop, isFloor):
    # sand start = (500,0)
    sand = [500,0]
    
    while True:
        
        if isFloor and sand[1] == stop[1]+1: 
            grid[tuple(sand)] = SAND
            return True
        
        sand[1] += 1
        if sand[1] == stop[1]+1:
            sand[1] -= 1
            grid[tuple(sand)] = SAND
            return True

        if tuple(sand) not in grid.keys(): 
            return False

        if grid[tuple(sand)] == AIR: continue
        
        # hit rock or sand
        # try left first
        sand[0] -= 1
        if tuple(sand) not in grid.keys():
            if not isFloor:
                return False
            grid, start, stop = addColumn(grid, sand[0], start, stop)
        
        if grid[tuple(sand)] == AIR:
            continue
        
        # try right
        sand[0] += 2
        if tuple(sand) not in grid.keys(): 
            if not isFloor: 
                return False
            grid, start, stop = addColumn(grid, sand[0], start, stop)

        if grid[tuple(sand)] == AIR:
            continue
        
        sand[0] -= 1
        sand[1] -= 1
        if sand[1] == stop[1]:
            grid[tuple(sand)] = SAND
            return True

        grid[tuple(sand)] = SAND
        return sand != [500,0]
            

def getAnswer(input):
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    grid, start, stop = buildGrid(input)
    # printGrid(grid, start, stop)

    while generateSand(grid, start, stop, False):
        answer[0] += 1

    # printGrid(grid, start, stop)

    grid = {}
    grid, start, stop = buildGrid(input)
    grid, start, stop = part2Grid(grid, start, stop)
    
    answer[1] = 1
    while generateSand(grid, start, stop, True):
        answer[1] += 1
    
    # printGrid(grid, start, stop)

    return answer

while(True):
    ans = getAnswer(menu())
    print('\nanswer: {}'.format(ans))
