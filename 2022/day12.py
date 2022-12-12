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

def printGrid(g, rev=False):
    if rev:
        for r in reversed(g):
            print(''.join(r))
    else:
        for r in g:
            print(''.join(str(r)))

def findCell(grid, letter):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == letter: return [r,c]
    return None

def calcManhatten(grid, start, end):
    m = []
    for r in range(len(grid)):
        row = []
        for c in range(len(grid[0])):
            row.append(abs(end[0] - r) + abs(end[1] - c))
        m.append(row)
    return m

def getAnswer(input):
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2
    
    grid = list(map(list, input))
    start = findCell(grid, 'S')
    end = findCell(grid, 'E')

    manhatten = calcManhatten(grid, start, end)
    
    

    answer[0] = 0
    answer[1] = 0

    return answer

while(True):
    ans = getAnswer(menu())
    print('\nanswer: {}'.format(ans))
