import sys
from functools import lru_cache

class Graph:
    def __init__(self, data):
        self.data = data
        self.numRows = len(data)
        self.numCols = len(data[0])
        self.nodes = []
        count = 1
        for row in range(self.numRows):
            for col in range(self.numCols):
                self.nodes.append(Node(count, int(data[row][col]), row, col))
                count += 1
        for n in self.nodes:
            n.addConnections(self)
    
    def getNodeByRowCol(self, row, col):
        for n in self.nodes:
            if n.row == row and n.col == col:
                return n
    
    def findAllPaths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.nodes:
            return []
        paths = []
        for node in start.neighbors:
            if node not in path:
                newpaths = self.findAllPaths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
                    print('adding path, curr count = ', len(paths))
        return paths

    def findShortestPath(self, start, end):
        paths = self.findAllPaths(start, end)
        scost = sys.maxsize
        spath = []
        for p in paths:
            cost = self.getPathCost(p)
            if cost < scost:
                scost = cost
                spath = p
        
        return spath

    @lru_cache(maxsize=None)
    def getPathCost(self, path):
        cost = 0
        for n in path:
            if n.id != 1:
                cost += n.cost
        return cost

class Node:
    def __init__(self, id, cost, row, col):
        self.id = id
        self.cost = cost
        self.row = row
        self.col = col
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.neighbors = []

    def __eq__(self, __o: object) -> bool:
        return self.id == __o.id

    def __hash__(self):
        return id(self)

    def __str__(self):
        return f'{self.id}'# ({self.row},{self.col}): ${self.cost}'

    def addConnections(self, graph: Graph):
        l = self.col - 1
        r = self.col + 1
        u = self.row - 1
        d = self.row + 1
        if l >= 0 and l < graph.numCols:
            self.left = graph.getNodeByRowCol(self.row, l)
            self.neighbors.append(self.left)
        if r >= 0 and r < graph.numCols:
            self.right = graph.getNodeByRowCol(self.row, r)
            self.neighbors.append(self.right)
        if u >= 0 and u < graph.numRows:
            self.up = graph.getNodeByRowCol(u, self.col)
            self.neighbors.append(self.up)
        if d >= 0 and d < graph.numRows:
            self.down = graph.getNodeByRowCol(d, self.col)
            self.neighbors.append(self.down)

f = open("sample.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

data = [list(d) for d in data]

def print_data():
    for r in range(len(data)):
        line = ""
        for c in range(len(data)):
            line += str(data[r][c])
        print(line)

paths = []

g = Graph(data)
print(f'{g.numRows}x{g.numCols}')
print(f'{len(g.nodes)} nodes in graph')

start = g.getNodeByRowCol(0,0)
end = g.getNodeByRowCol(len(data)-1, len(data[0])-1)
print(f'{start} -> {end}')

path = g.findShortestPath(start, end)
cost = g.getPathCost(path)

print(f'path cost: {cost}')
