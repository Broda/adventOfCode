import sys
from functools import lru_cache

class Graph:
    def __init__(self, data):
        self.data = data
        self.numRows = len(data)
        self.numCols = len(data[0])
        self.nodes = {}
        self.count = 0
        
        for row in range(self.numRows):
            for col in range(self.numCols):
                self.nodes[(row,col)] = {'cost':int(data[row][col]), 'connections':[]}
                if row > 0:
                    self.nodes[(row,col)]['connections'].append((row-1,col))
                if row + 1 < self.numRows - 1:
                    self.nodes[(row,col)]['connections'].append((row+1,col))
                if col > 0:
                    self.nodes[(row,col)]['connections'].append((row,col-1))
                if col + 1 < self.numCols - 1:
                    self.nodes[(row,col)]['connections'].append((row,col+1))
                    
    def findAllPaths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.nodes.keys():
            return []
        paths = []
        self.count += 1
        if self.count > 10000:
            return paths

        for node in self.nodes[start]['connections']:
            if node not in path:
                #print(f'node {node} not in path {path}, finding new paths from node to end')
                newpaths = self.findAllPaths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
                    #print(f'adding path {newpath}, curr count = {len(paths)}')
        return paths

    @lru_cache(maxsize=None)
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

    def getPathCost(self, path):
        cost = 0
        for n in path:
            if n != (0,0):
                cost += self.nodes[n]['cost']
        return cost

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

start = (0,0)
end = (len(data)-1, len(data[0])-1)
print(f'{start} -> {end}')

# for n in g.nodes:
#     print(f'{n}: {g.nodes[n]}')

path = g.findShortestPath(start, end)
print(path)
cost = g.getPathCost(path)
print(f'path cost: {cost}')
