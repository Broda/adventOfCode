import os
import sys
import heapq
import itertools

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

class Graph:
    def __init__(self, data : list) -> None:
        self.parseData(data.copy())
    
    def getNeighbors(self, node : tuple, rawData : list) -> list:
        neighbors : list = []
        x, y = node
        if x-1 >= 0:
            if rawData[y][x-1] != "#":
                neighbors.append((x-1,y))
        if y-1 >= 0:
            if rawData[y-1][x] != "#":
                neighbors.append((x,y-1))
        if x+1 < len(rawData[0]):
            if rawData[y][x+1] != "#":
                neighbors.append((x+1,y))
        if y+1 < len(rawData):
            if rawData[y+1][x] != "#":
                neighbors.append((x,y+1))
        return neighbors.copy()

    def parseData(self, data :list) -> None:
        self.start : tuple = ()
        self.targets : list = []
        self.data : dict = {}

        for r in range(len(data)):
            for c in range(len(data[0])):
                if data[r][c] == "#": continue
                self.data[(c, r)] = self.getNeighbors((c, r), data)
                if data[r][c] == "0":
                    self.start = (c, r)
                elif data[r][c].isdigit() and (c, r) not in self.targets:
                    self.targets.append((c,r))

    def printGraph(self):
        print(f"Start: {self.start}")
        print(f"Targets: {self.targets}")
        keys = list(self.data.keys())
        maxR = max(keys, key=lambda x: x[1])[1]
        maxC = max(keys, key=lambda x: x[0])[0]
        for r in range(maxR+2):
            row = ""
            for c in range(maxC+2):
                if (c, r) == self.start:
                    row += "S"
                elif (c, r) in self.targets:
                    row += "T"
                elif (c, r) not in self.data.keys():
                    row += "#"
                else:
                    row += "."
            print(row)
            
    def shortestPathToAll(self) -> list:
        best : list = None
        shortestDist : float = float('inf')

        for perm in itertools.permutations(self.targets):
            curr = self.start
            currPath = [self.start]
            totalDist = 0

            for next in perm:
                path = self.shortestPath(curr, next)
                if path is None: break
                currPath.extend(path[1:])
                totalDist += self.calcDist(path)
                curr = next
            
            if path is not None and totalDist < shortestDist:
                shortestDist = totalDist
                best = currPath
        
        return best, shortestDist
            
    def shortestPath(self, start : tuple, end : tuple) -> list:
        if start == end: return [start]

        queue = [(start, [start])]
        visited = {start}

        while queue:
            (vertex, path) = queue.pop(0)
            for neighbor in self.data[vertex]:
                if neighbor == end:
                    return path + [end]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None
    
    def calcDist(self, path : list) -> int:
        dist = 0
        for i in range(len(path) - 1):
            if path[i+1] in self.data[path[i]]:
                dist += 1
            else:
                return float('inf')
        return dist

    def shortestPathToAllAndReturn(self) -> list:
        best : list = None
        minCost : float = float('inf')

        for perm in itertools.permutations(self.targets):
            path = [self.start] + list(perm) + [self.start]
            cost = 0
            currPath = []

            for i in range(len(path) - 1):
                src, dest = path[i], path[i+1]
                shortestPath = self.shortestPath(src, dest)
                shortestCost = self.calcDist(shortestPath)
                if shortestPath is None:
                    cost = float('inf')
                    break
                cost += shortestCost
                currPath.extend(shortestPath[:-1] if i < len(path) - 2 else shortestPath)

            if cost < minCost:
                minCost = cost
                best = currPath
        return best, minCost
    
def getPart1(input : list) -> int:
    g : Graph = Graph(input)

    return g.shortestPathToAll()[1]

def getPart2(input : list) -> int:
    g : Graph = Graph(input)

    return g.shortestPathToAllAndReturn()[1]

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2


    answer[0] = getPart1(input)
    answer[1] = getPart2(input)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
