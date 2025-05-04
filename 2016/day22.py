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
    if not os.getcwd().endswith('2016'): os.chdir('2016')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2016'): os.chdir('2016')
    f = open(path, 'w')
    f.write(s)
    f.close()

class Node:
    def __init__(self, data : str) -> None:
        path, size, used, avail, percent = data.split()
        _, x, y = path.split("-")
        self.x = int(x[1:])
        self.y = int(y[1:])
        self.size = int(size[0:len(size)-1])
        self.used = int(used[0:len(used)-1])
        self.avail = int(avail[0:len(avail)-1])
        self.percent = int(percent[0:len(percent)-1])

    def position(self) -> tuple:
        return (self.x, self.y)
    
    def neighbors(self, gridSize : tuple) -> list:
        n = []
        if self.x - 1 >= 0: n.append((self.x-1,self.y))
        if self.y - 1 >= 0: n.append((self.x, self.y-1))
        if self.x + 1 < gridSize[0]: n.append((self.x+1,self.y))
        if self.y + 1 < gridSize[0]: n.append((self.x,self.y+1))
        return n

    def dataCanFit(self, amt) -> bool:
        if amt <= self.avail: return True

    def tryMoveData(self, dest) -> bool:
        if not isinstance(dest, Node): return False
        if dest.avail >= self.used:
            dest.loadData(self.used)
            self.unloadData()
            return True
    
    def loadData(self, amt : int) -> None:
        self.used += amt
        self.avail -= amt
        self.percent = (self.used // self.size) * 100

    def unloadData(self) -> None:
        self.used = 0
        self.avail = self.size
        self.percent = 0

    def __str__(self) -> str:
        return f"({self.x},{self.y})\t{self.size}T\t{self.used}T\t{self.avail}T\t{self.percent}%"

    def __repr__(self):
        return f"({self.x},{self.y})\t{self.size}T\t{self.used}T\t{self.avail}T\t{self.percent}%"

    def __eq__(self, n) -> bool:
        if not isinstance(n, Node): return False
        return self.position() == n.position()
    
def getGridMaxes(nodes : dict) -> tuple:
    maxX = 0
    maxY = 0
    for x,y in nodes.keys():
        if x > maxX: maxX = x
        if y > maxY: maxY = y
    return (maxX, maxY)

def loadNodes(input : list) -> dict:
    nodes = {}
    for line in input:
        if not line.startswith("/dev/grid/node"): continue
        n = Node(line)
        nodes[n.position()] = n

    return nodes

def getViablePairs(nodes : dict) -> list:
    pairs = []
    for k in nodes.keys():
        n : Node = nodes[k]
        if n.used == 0: continue
        for k2 in nodes.keys():
            if k == k2: continue
            n2 : Node = nodes[k2]
            if n.used <= n2.avail:
                pairs.append((k, k2))
    return pairs

def getPart1(nodes : dict) -> int:
    pairs = getViablePairs(nodes)

    return len(pairs)

def findEmptyNode(nodes : dict) -> tuple:
    for k in nodes.keys():
        n : Node = nodes[k]
        if n.percent == 0: return k

def printGrid(nodes : dict, maxes : tuple, empty : list, dataLoc : list) -> None:
    for y in range(maxes[1]+1):
        line = ""
        for x in range(maxes[0]+1):
            if x == dataLoc[0] and y == dataLoc[1]:
                line += "D"
            elif x == 0 and y == 0:
                line += "G"
            elif empty == [x, y]:
                line += "_"
            elif nodes[(x,y)].size >= 100:
                line += "#"
            else:
                line += "."
        print(line)

def getPart2(nodes : dict) -> int:
    maxes = getGridMaxes(nodes)
    empty = list(findEmptyNode(nodes))
    dataLoc = [maxes[0],0]
    print(empty)
    print(maxes)
    printGrid(nodes, maxes, empty, dataLoc)
    return 27 + (maxes[0]-1)*5

    steps = 0
    
    for x in range(empty[0]+1, maxes[0]+1, 1):
        y = empty[1]
        n : Node = nodes[(x,y)]
        if n.tryMoveData(nodes[tuple(empty)]):
            if dataLoc == [x,y]:
                dataLoc[0] = empty[0]
            empty[0] = x
            steps += 1

    for y in range(empty[1], -1, -1):
        x = empty[0]
        n : Node = nodes[(x,y)]
        if n.tryMoveData(nodes[tuple(empty)]): 
            if dataLoc == [x,y]:
                dataLoc[0] = empty[0]
            empty[1] = y
            steps += 1
    
    while dataLoc != [0,0]:
        n : Node = nodes[(empty[0],empty[1]+1)]
        n.tryMoveData(nodes[tuple(empty)])
        empty[1] += 1
        steps += 1
        n = nodes[(empty[0]-1,empty[1])]
        n.tryMoveData(nodes[tuple(empty)])
        empty[0] -= 1
        steps += 1
        n = nodes[(empty[0]-1,empty[1])]
        n.tryMoveData(nodes[tuple(empty)])
        empty[0] -= 1
        steps += 1
        n = nodes[(empty[0],empty[1]-1)]
        n.tryMoveData(nodes[tuple(empty)])
        empty[1] -= 1
        steps += 1
        n = nodes[tuple(dataLoc)]
        n.tryMoveData(nodes[tuple(empty)])
        dataLoc = empty.copy()
        empty[0] += 1
        steps += 1

    printGrid(nodes, maxes, empty, dataLoc)
    return steps

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2
    
    nodes = loadNodes(input)
    answer[0] = getPart1(nodes)
    answer[1] = getPart2(nodes)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
