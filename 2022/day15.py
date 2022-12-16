import os
import sys
from copy import deepcopy

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


def calcManhatten(start, end):
    return abs(end[0] - start[0]) + abs(end[1] - start[1])


def buildGrid(input):
    g = {}
    for l in input:
        _, _, sx, sy, _, _, _, _, bx, by = l.split()
        sx = int(sx.split('=')[1][:-1])
        sy = int(sy.split('=')[1][:-1])
        bx = int(bx.split('=')[1][:-1])
        by = int(by.split('=')[1])
        g[(sx, sy)] = ('S', calcManhatten((sx, sy), (bx, by)))        
        g[(bx, by)] = 'B'
    return g

def countBlockedSpotsInRow(grid, y):
    count = 0
    spots = {}
    for k, p in grid.items():
        # k = (x, y), p[0] = 'S', p[1] = manhatten dist
        if type(p) is tuple:
            diff = abs(k[1] - y)
            if diff > p[1]:
                continue
            
            x_diff = p[1] - diff
                        
            for x in range(k[0]-x_diff, k[0] + x_diff+1):
                if (x, y) in grid.keys():
                    spots[(x,y)] = grid[(x,y)]

                if (x,y) not in spots.keys():
                    count += 1
                    spots[(x,y)] = '#'

        elif k[1] == y:
            spots[k] = 'B'

    return count

def markSensorRange(grid):
    init_grid = deepcopy(grid)

    for k, p in init_grid.items():
        if type(p) is tuple:
            x_mod = 0
            for y in range(k[1]-p[1], k[1]+p[1]+1):
                for x in range(k[0]-x_mod, k[0]+x_mod+1):
                    if (x, y) not in grid.keys():
                        grid[(x, y)] = '#'

                if y >= k[1]:
                    x_mod -= 1
                else:
                    x_mod += 1

    return grid

def findBeacon(grid):
    grid = markSensorRange(grid)

    for y in range(4000001):
        for x in range(4000001):
            if (x,y) not in grid.keys():
                return x * 4000000 + y

def getAnswer(input, isSample):
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    grid = buildGrid(input)

    if isSample:
        answer[0] = countBlockedSpotsInRow(grid, 10)
        answer[1] = findBeacon(grid)
    else:
        answer[0] = countBlockedSpotsInRow(grid, 2000000)

    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
