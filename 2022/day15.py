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

def calcManhatten(start, end):
    return abs(end[0] - start[0]) + abs(end[1] - start[1])

# def tryUpdateStartStop(newPos, start, stop):
#     start[0] = min(start[0], newPos[0])
#     start[1] = min(start[1], newPos[1])
#     stop[0] = max(stop[0], newPos[0])
#     stop[1] = max(stop[1], newPos[1])
#     return start, stop

# def markSensorRange(grid, sensor, beacon, start, stop):
#     dist = calcManhatten(sensor, beacon)
#     x_mod = 0
#     for y in range(sensor[1]-dist, sensor[1]+dist+1):
#         for x in range(sensor[0]-x_mod, sensor[0]+x_mod+1):
#             if (x, y) not in grid.keys():
#                 #print('adding ({},{})'.format(x, y))
#                 grid[(x, y)] = '#'
#             elif grid[(x, y)] == '.':
#                 grid[(x, y)] = '#'
#             start, stop = tryUpdateStartStop((x, y), start, stop)
#         if y >= sensor[1]:
#             x_mod -= 1
#         else:
#             x_mod += 1

#     return grid, start, stop

# def countBlockedSpotsInRow(grid, y, start, stop):
#     count = 0
#     for x in range(start[0], stop[0]+1):
#         if (x, y) in grid.keys():
#             if grid[(x, y)] == '#': 
#                 count += 1
#         #     else:
#         #         print('({},{}) = "{}"'.format(x, y, grid[(x, y)]))
#         # else:
#         #     print('({},{}) not in grid'.format(x, y))

#     return count

# def buildGrid(input):
#     g = {}
#     start = [sys.maxsize, sys.maxsize]
#     stop = [-sys.maxsize, -sys.maxsize]
#     for l in input:
#         _, _, sx, sy, _, _, _, _, bx, by = l.split()
#         # print('sx="{}", sy="{}"'.format(sx, sy))
#         sx = int(sx.split('=')[1][:-1])
#         sy = int(sy.split('=')[1][:-1])
#         # print('sx="{}", sy="{}"'.format(sx, sy))
#         # print('bx="{}", by="{}"'.format(bx, by))
#         bx = int(bx.split('=')[1][:-1])
#         by = int(by.split('=')[1])
#         # print('bx="{}", by="{}"'.format(bx, by))
#         g[(sx, sy)] = 'S'
#         start, stop = tryUpdateStartStop((sx, sy),start, stop)
        
#         g[(bx, by)] = 'B'
#         start, stop = tryUpdateStartStop((bx, by),start, stop)
        
#         g, start, stop = markSensorRange(g, (sx, sy), (bx, by), start, stop)

#     return g, start, stop


# def printGrid(grid, start, stop):
#     print_grid_str = ''
#     for y in range(start[1],stop[1]+1):
#         r = ''
#         for x in range(start[0], stop[0]+1):
#             if (x, y) in grid.keys():
#                 r += grid[(x,y)]
#             else:
#                 r += '.'

#         print_grid_str += r + '\n'

#     print(print_grid_str)

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
    #2 * (dist - abs(sensor_y - line_y)) + 1 = num blocked spots
    #if num blocked spots < 0, num blocked spots = 0
    count = 0
    for k, p in grid.items():
        if type(p) is tuple:
            spots = 2 * (p[1] - abs(k[1] - y))
            if spots > 0: count += spots + 1
        elif k[1] == y:
            count -= 1 # remove any B on line

    return count

def readFile(path):
    if not os.getcwd().endswith('2022'): os.chdir('2022')
    f = open(path, "r")
    return f.read().strip()

def getAnswer(input, isSample):
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    #grid, start, stop = buildGrid(input)
    #printGrid(grid, start, stop)
    grid = buildGrid(input)

    # if isSample:
    #     answer[0] = countBlockedSpotsInRow(grid, 10, start, stop)
    # else:
    #     answer[0] = countBlockedSpotsInRow(grid, 2000000, start, stop)
    if isSample:
        answer[0] = countBlockedSpotsInRow(grid, 10)
    else:
        answer[0] = countBlockedSpotsInRow(grid, 2000000)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
