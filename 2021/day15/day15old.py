from copy import deepcopy

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

class Path:
    def __init__(self, data):
        self.data = data
        self.nodes = [(0,0)]
        self.score = 0
        self.complete = False
        self.end = (len(data)-1, len(data[0])-1)

    def addNode(self, n):
        if self.complete:
            return

        if n in self.nodes:
            return

        self.nodes.append(n)
        self.score += int(self.data[n[0]][n[1]])
        if self.end == n:
            self.complete = True

    def __eq__(self, __o: object) -> bool:
        if len(self.nodes) != len(__o.nodes):
            return False
        for n in range(len(self.nodes)):
            if self.nodes[n] != __o.nodes[n]:
                return False
        return True

def validNode(node):
    if node[0] < 0 or node[0] > len(data)-1:
        return False
    if node[1] < 0 or node[1] > len(data[0])-1:
        return False
    return True

def findPath(paths: list, path: Path):
    if len(paths) > 200:
        return
    if path.complete:
        if path not in paths:
            paths.append(path)
        return

    currNode = path.nodes[-1]
    left = (currNode[0], currNode[1] - 1)
    right = (currNode[0], currNode[1] + 1)
    up = (currNode[0]-1, currNode[1])
    down = (currNode[0]+1, currNode[1])
    if validNode(left) and left not in path.nodes:
        pNew = deepcopy(path)
        pNew.addNode(left)
        findPath(paths, pNew)
    if validNode(right) and right not in path.nodes:
        pNew = deepcopy(path)
        pNew.addNode(right)
        findPath(paths, pNew)
    if validNode(up) and up not in path.nodes:
        pNew = deepcopy(path)
        pNew.addNode(up)
        findPath(paths, pNew)
    if validNode(down) and down not in path.nodes:
        pNew = deepcopy(path)
        pNew.addNode(down)
        findPath(paths, pNew)
    return

findPath(paths, Path(data))
for p in paths:
    print(f'num nodes: {len(p.nodes)}, score: {p.score}')