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
    if not os.getcwd().endswith('2024'): os.chdir('2024')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2024'): os.chdir('2024')
    f = open(path, 'w')
    f.write(s)
    f.close()

def addTuples(t1 : tuple, t2 : tuple) -> tuple:
    return (t1[0] + t2[0], t1[1] + t2[1])

def getBoardValue(board : list, pos : tuple) -> int:
    return board[pos[0]][pos[1]]

class Node:
    def __init__(self, loc : tuple, value : int, board: list):
        self.loc = loc
        self.value = value
        self.board = board
        self.boardSize = (len(board), len(board[0]))
        self.neighbors = []
        self.tryAddNeighbors()
    
    def tryAddNeighbor(self, n : tuple):
        v = getBoardValue(self.board, n)
        if v == self.value + 1:
            self.neighbors.append(Node(n, v, self.board))
            
    def tryAddNeighbors(self):
        if self.loc[0] > 0: #up
            self.tryAddNeighbor(addTuples(self.loc, (-1, 0)))
        if self.loc[0]+1 < self.boardSize[0]: #down
            self.tryAddNeighbor(addTuples(self.loc, (1, 0)))
        if self.loc[1] > 0: #left
            self.tryAddNeighbor(addTuples(self.loc, (0, -1)))
        if self.loc[1]+1 < self.boardSize[1]: #right
            self.tryAddNeighbor(addTuples(self.loc, (0, 1)))
            
    
def buildPaths(root : Node) -> list:
    def depthFirst(node : Node, path : list, result : list):
        if not node:
            return
        path.append(node.loc)
        if len(node.neighbors) == 0:
            result.append(path.copy())
        for n in node.neighbors:
            depthFirst(n, path, result)
        
        path.pop()

    result = []
    depthFirst(root, [], result)
    return result

def getPart1(board : list) -> int:
    trails = {}
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 0:
                print(f"adding root @ ({r},{c})")
                root = Node((r,c), 0, board)
                trails[(r,c)] = buildPaths(root)
    
    sum = 0
    for k in trails.keys():
        diff_9s = []
        for p in trails[k]:
            if getBoardValue(board, p[-1]) == 9 and p[-1] not in diff_9s:
                diff_9s.append(p[-1])
        sum += len(diff_9s)
            
    return sum

def getPart2(board : list) -> int:
    trails = {}
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 0:
                print(f"adding root @ ({r},{c})")
                root = Node((r,c), 0, board)
                trails[(r,c)] = buildPaths(root)
    
    sum = 0
    for k in trails.keys():
        for p in trails[k]:
            if getBoardValue(board, p[-1]) == 9:
                sum += 1
            
    return sum

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    board = [[int(x) for x in row] for row in input]
    
    answer[0] = getPart1(board)
    answer[1] = getPart2(board)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
