import os
import sys
from statistics import variance

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

class Robot:
    def __init__(self, pvStr : str):
        self.init = pvStr
        self.pos = [int(p) for p in pvStr.split(" ")[0].split("=")[1].split(",")]
        self.vel = [int(p) for p in pvStr.split(" ")[1].split("=")[1].split(",")]
    
    def reset(self):
        self.pos = [int(p) for p in self.init.split(" ")[0].split("=")[1].split(",")]
        self.vel = [int(p) for p in self.init.split(" ")[1].split("=")[1].split(",")]
    
    def move(self, boardSize : tuple, times : int):
        self.pos[0] = (self.pos[0] + self.vel[0] * times) % boardSize[0]
        self.pos[1] = (self.pos[1] + self.vel[1] * times) % boardSize[1]

    def sim(self, boardSize : tuple, times : int):
        return ((self.pos[0] + self.vel[0] * times) % boardSize[0], (self.pos[1] + self.vel[1] * times) % boardSize[1])
    
    def __repr__(self) -> str:
        return f"p={self.pos}, v={self.vel}"
    
def countRobots(robots : list, boardMin : tuple, boardMax : tuple) -> int:
    num = 0
    
    for r in robots:
        if r.pos[0] >= boardMin[0] and r.pos[0] < boardMax[0] and r.pos[1] >= boardMin[1] and r.pos[1] < boardMax[1]:
            num += 1
    return num

def printBoard(boardSize : tuple, robots : list):
    board = [[0 for i in range(boardSize[0])] for j in range(boardSize[1])]
    mid = (boardSize[0]//2, boardSize[1]//2)
    
    for r in robots:
        board[r.pos[1]][r.pos[0]] += 1
        
    for y in range(boardSize[1]):
        row = ""
        if y != mid[1]:
            for x in range(boardSize[0]):
                if x == mid[0]:
                    row += " "
                else:
                    row += str(board[y][x])
        print(row.replace("0", "."))
            
def getPart1(robots : list, isSample : bool = False) -> int:
    #100 seconds
    boardSize = (101, 103)
    if isSample:
        boardSize = (11, 7)
        
    for r in robots:
        r.move(boardSize, 100)
    
    mid = (boardSize[0]//2, boardSize[1]//2)
    
    q1 = countRobots(robots, (0, 0), (mid[0], mid[1]))
    q2 = countRobots(robots, (mid[0]+1, 0), (boardSize[0], mid[1]))
    q3 = countRobots(robots, (0, mid[1]+1), (mid[0], boardSize[1]))
    q4 = countRobots(robots, (mid[0]+1, mid[1]+1), (boardSize[0], boardSize[1]))
    
    return q1 * q2 * q3 * q4

def getPart2(robots : list) -> int:
    boardSize = (101, 103)

    minVar = [10000,10000]
    x, y = 0, 0
    for it in (range(max(boardSize[0],boardSize[1]))):
        robot_locs = [r.sim(boardSize, it) for r in robots]
        robot_xs, robot_ys = zip(*robot_locs)
        xvar = variance(robot_xs)
        yvar = variance(robot_ys)
        if xvar < minVar[0]:
            minVar[0] = xvar
            x = it
        if yvar < minVar[1]:
            minVar[1] = yvar
            y = it
    # Chinese Remainder Theorem
    return x+((pow(boardSize[0], -1, boardSize[1])*(y-x)) % boardSize[1])*boardSize[0]

def loadRobots(input : list) -> list:
    #p=0,4 v=3,-3
    robots = []
    for r in input:
        robots.append(Robot(r))
    return robots
    
def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    answer[0] = getPart1(loadRobots(input), isSample)
    answer[1] = getPart2(loadRobots(input))
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
