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

def tupleSub(t1, t2):
    return (t1[0]-t2[0],t1[1]-t2[1])

class Blizzard:
    def __init__(self, loc, dir, gridSize) -> None:
        self.loc = loc
        self.dir = dir
        self.gridSize = gridSize

    def move(self):
        match self.dir:
            case '^':
                self.loc = tupleAdd(self.loc, (0,-1))
                if self.loc[1] <= 0: self.loc = (self.loc[0], self.gridSize[1]-2) 
            case 'v':
                self.loc = tupleAdd(self.loc, (0,1))
                if self.loc[1] >= self.gridSize[1]-1: self.loc = (self.loc[0], 1)
            case '<':
                self.loc = tupleAdd(self.loc, (-1,0))
                if self.loc[0] <= 0: self.loc = (self.gridSize[0]-2, self.loc[1])
            case '>':
                self.loc = tupleAdd(self.loc, (1,0))
                if self.loc[0] >= self.gridSize[0]-1: self.loc = (1, self.loc[1])

    def __str__(self) -> str:
        return self.dir

def buildGrid(input):
    grid = {}
    size_x = len(input[0])
    size_y = len(input)
    start = (input[0].index('.'),0)
    end = (input[-1].index('.'), size_y-1)

    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == '.':
                grid[(x,y)] = []
            elif input[y][x] == '#':
                grid[(x,y)] = '#'
            else:
                grid[(x,y)] = [Blizzard((x,y), input[y][x], (size_x, size_y))]
    
    return grid, start, end, size_x, size_y

def printGrid(grid, size_x, size_y):
    for y in range(size_y):
        s = ''
        for x in range(size_x):
            if type(grid[(x,y)]) is list:
                if len(grid[(x,y)]) > 1:
                    s += str(len(grid[(x,y)]))
                elif len(grid[(x,y)]) == 1:
                    s += str(grid[(x,y)][0])
                else:
                    s += '.'
            else:
                s += grid[(x,y)]
        print(s)



def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    grid, start, end, size_x, size_y = buildGrid(input)
    print('Start: {}, End: {}'.format(start, end))
    printGrid(grid, size_x, size_y)



    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))



