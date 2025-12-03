import sys
import os
import re

def readFile(path):
    if not os.getcwd().endswith('2022'): os.chdir('2022')
    f = open(path, "r")
    return f.read().strip()

def printGrid(g):
    for r in g:
        print(r)

def menu(samplePath, inputPath):
    main = "\nPlease choose an input option:\n"
    main += "1. Sample File\n"
    main += "2. Input File\n"
    main += "3. Other File\n"
    main += "4. Prompt\n"
    main += "5. Quit\n"
    main += ">> "
    
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

def treeIsVisible(g, rowIndex, colIndex):
    # perimeter tree
    if rowIndex == 0 or rowIndex == len(g)-1 or colIndex == 0 or colIndex == len(g[0]) - 1: return True
    curr = int(g[rowIndex][colIndex])
    visLeft = True
    visRight = True
    visUp = True
    visDown = True
    for c in range(len(g[0])):
        if c == colIndex: continue
        n = int(g[rowIndex][c])
        if n >= curr:
            if c < colIndex:
                visLeft = False
            if c > colIndex:
                visRight = False
        #print(s)
    for r in range(len(g)):
        if r == rowIndex: continue
        n = int(g[r][colIndex])
        if n >= curr:
            if r < rowIndex:
                visUp = False
            if r > rowIndex:
                visDown = False
        #print(s)
    return visLeft or visRight or visUp or visDown

def getVisibleCount(g):
    count = 0
    for r in range(len(g)):
        for c in range(len(g[0])):
            if treeIsVisible(g, r, c): 
                count += 1
    return count

def getScenicScore(g, rowIndex, colIndex):
    distLeft = 0
    distRight = 0
    distUp = 0
    distDown = 0
    tree = int(g[rowIndex][colIndex])

    # count up
    for r in range(rowIndex-1,-1,-1):
        distUp += 1
        n = int(g[r][colIndex])
        if n >= tree: break
    
    # count down
    for r in range(rowIndex+1,len(g)):
        distDown += 1
        n = int(g[r][colIndex])
        if n >= tree: break

    # count left
    for c in range(colIndex-1,-1,-1):
        distLeft += 1
        n = int(g[rowIndex][c])
        if n >= tree: break
    
    # count right
    for c in range(colIndex+1,len(g[0])):
        distRight += 1
        n = int(g[rowIndex][c])
        if n >= tree: break

    return distLeft * distRight * distUp * distDown

def getMaxScore(g):
    max = 0
    for r in range(len(g)):
        for c in range(len(g[0])):
            score = getScenicScore(g, r, c)
            if score > max: max = score
    return max

def getAnswer(input):
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2
    
    grid = []
    vGrid = []
    for l in input:
        grid.append([*l])
        vGrid.append([False] * len(grid[0]))
    
    answer[0] = getVisibleCount(grid)
    answer[1] = getMaxScore(grid)

    return answer

while(True):
    ans = getAnswer(menu('day08sample.txt','day08input.txt'))
    print('\nanswer: {}'.format(ans))
