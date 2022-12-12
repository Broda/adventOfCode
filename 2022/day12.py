import os
import sys
import collections

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
            return readFile(samplePath)
        case "2":
            return readFile(inputPath)
        case "3":
            return readFile(input("File Name: "))
        case "4":
            return input("Input: ")
        case _:
            print("Invalid option. Try Again.\n")
            return menu()

def readFile(path):
    if not os.getcwd().endswith('2022'): os.chdir('2022')
    f = open(path, "r")
    return f.read().strip()

def bfs(grid, *start):
    
    q = collections.deque((row, col, 0, 'a') for row in range(len(grid))
        for col in range(len(grid[0]))
        if grid[row][col] in start)

    visited = set((row, col) for row, col, count, char in q)

    def push(row, col, count, curr):
        if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])): return
        if (row, col) in visited: return

        next = grid[row][col].replace('E', 'z') # replace E if we're checking the end
        if ord(next) > ord(curr) + 1: return
        
        visited.add((row, col))
        q.append((row, col, count + 1, next))

    while len(q):
        row, col, count, char = q.popleft()
        if grid[row][col] == 'E': return count
        
        push(row + 1, col, count, char)
        push(row - 1, col, count, char)
        push(row, col + 1, count, char)
        push(row, col - 1, count, char)

def getAnswer(input):
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2
    
    grid = list(map(list, input))
    
    answer[0] = bfs(grid, 'S')
    answer[1] = bfs(grid, 'a')

    return answer

while(True):
    ans = getAnswer(menu())
    print('\nanswer: {}'.format(ans))
