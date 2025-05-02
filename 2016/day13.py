import os
import sys
from collections import deque

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

def is_open_space(loc : tuple, input : int) -> bool:
    x, y = loc
    val : int = x*x + 3*x + 2*x*y + y + y*y + input
    #print(f"is_open_space({loc}, {input}): val = {val}, bitcount = {val.bit_count()}, even = {val.bit_count() % 2 == 0}")
    return val.bit_count() % 2 == 0

def get_grid_neighbors(node : tuple, input : int) -> list:
    x, y = node
    neighbors = []
    if is_open_space((x+1,y), input):
        neighbors.append((x+1,y))
    if is_open_space((x, y+1), input):
        neighbors.append((x,y+1))
    if x > 0: 
        if is_open_space((x-1,y), input):
            neighbors.append((x-1,y))
    if y > 0: 
        if is_open_space((x, y-1), input):
            neighbors.append((x,y-1))
        
    return neighbors

def bfs_infinite_graph(startNode : tuple, dest : tuple, get_neighbors : callable, input : int):
    queue = deque([(startNode, [startNode], 0)])
    visited = {startNode}

    while queue:
        curr, path, steps = queue.popleft()
        
        if steps == 50:
            print(f"visited after 50 steps: {len(visited)}")

        if curr == dest:
            return path
        
        for neighbor in get_neighbors(curr, input):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor], steps+1))
        
    return None
    
def getPart1(input : int, dest : tuple) -> int:
    start : tuple = (1,1)
    path = bfs_infinite_graph(start, dest, get_grid_neighbors, input)
    if path:
        #print(f"Shortest path: {path}")
        return len(path)-1
    else:
        print("No path found.")
        return 0


def getPart2(input : int) -> int:

    return 0

def getAnswer(input, isSample) -> list:
    input = int(input.replace("\r", "").split("\n")[0])
    answer = [0,0] #part1, part2

    dest = (31,39)
    if isSample: dest = (7,4)
    answer[0] = getPart1(input, dest)
    answer[1] = getPart2(input)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
