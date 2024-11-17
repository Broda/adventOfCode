import os
import sys
import functools

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
    if not os.getcwd().endswith('2023'): os.chdir('2023')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2023'): os.chdir('2023')
    f = open(path, 'w')
    f.write(s)
    f.close()

class Map():
    def __init__(self, lines) -> None:
        self.lines = [[*l] for l in lines]
        self.tiltNorth()
        self.northLoad = self.getNorthLoad()
        self.tiltSouth() # reset lines for part 2
        
    @functools.lru_cache
    def tiltNorth(self):
        print('tiltNorth')
        while self.moveRocks((0,-1)):
            pass
    
    @functools.lru_cache
    def tiltWest(self):
        print('tiltWest')
        while self.moveRocks((-1,0)):
            pass

    @functools.lru_cache
    def tiltSouth(self):
        print('tiltSouth')
        count = 0
        while self.moveRocks((0,1)):
            pass
    
    @functools.lru_cache
    def tiltEast(self):
        print('tiltEast')
        while self.moveRocks((1,0)):
            pass

    @functools.lru_cache
    def spin(self, numCycles):
        for i in range(numCycles):
            self.spinCycle()
            if i % 10 == 0: print(i)

    @functools.lru_cache
    def spinCycle(self):
        self.tiltNorth()
        self.tiltWest()
        self.tiltSouth()
        self.tiltEast()

    @functools.lru_cache
    def moveRocks(self, direction):
        moveMade = False
        if direction[1] == -1:
            for i in range(len(self.lines)):
                newRow = i + direction[1]
                if newRow < 0 or newRow >= len(self.lines):
                    pass
                else:
                    for j in range(len(self.lines[0])):
                        if self.lines[i][j] == 'O' and self.lines[newRow][j] == '.':
                            self.lines[i][j] = '.'
                            self.lines[newRow][j] = 'O'
                            moveMade = True
        elif direction[1] == 1:
            for i in range(len(self.lines)-1,-1,-1):
                newRow = i + direction[1]
                if newRow < 0 or newRow >= len(self.lines):
                    pass
                else:
                    for j in range(len(self.lines[0])):
                        if self.lines[i][j] == 'O' and self.lines[newRow][j] == '.':
                            self.lines[i][j] = '.'
                            self.lines[newRow][j] = 'O'
                            moveMade = True
        
        elif direction[0] == -1:
            for j in range(len(self.lines[0])):
                newCol = j + direction[0]
                if newCol < 0 or newCol >= len(self.lines[0]):
                    pass
                else:
                    for i in range(len(self.lines)):
                        if self.lines[i][j] == 'O' and self.lines[i][newCol] == '.':
                            self.lines[i][j] = '.'
                            self.lines[i][newCol] = 'O'
                            moveMade = True
        else:
            for j in range(len(self.lines[0])-1,-1,-1):
                newCol = j + direction[0]
                if newCol < 0 or newCol >= len(self.lines[0]):
                    pass
                else:
                    for i in range(len(self.lines)):
                        if self.lines[i][j] == 'O' and self.lines[i][newCol] == '.':
                            self.lines[i][j] = '.'
                            self.lines[i][newCol] = 'O'
                            moveMade = True
        return moveMade

    @functools.lru_cache
    def getNorthLoad(self):
        sum = 0
        for j in range(len(self.lines[0])):
            for i in range(len(self.lines)):
                weight = len(self.lines) - i
                if self.lines[i][j] == 'O':
                    sum += weight
        return sum
        
def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    m = Map(input)
    m.spin(1000000000)

    answer[0] = m.northLoad
    answer[1] = m.getNorthLoad()
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))


