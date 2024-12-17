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

def findSymbols(input : list) -> dict:
    symbols = {}
    for r in range(len(input)):
        for c in range((len(input[0]))):
            if input[r][c] != ".":
                node = input[r][c]
                if node not in symbols.keys():
                    symbols[node] = [(c, r)]
                else:
                    symbols[node].append((c, r))
    return symbols

def addTuples(t1 : tuple, t2 : tuple) -> tuple:
    return (t1[0]+t2[0], t1[1]+t2[1])

def subTuples(t1 : tuple, t2 : tuple) -> tuple:
    return (t1[0]-t2[0], t1[1]-t2[1])

def getPart1(input : list) -> int:
    symbols = findSymbols(input)
    boardSize = (len(input[0]), len(input)) # (width, height)
    antis = []
    for k in symbols.keys():
        while len(symbols[k]) > 0:
            node = symbols[k].pop(0)
            for n in symbols[k]:
                slope = subTuples(n, node)
                anti1 = subTuples(node, slope)
                anti2 = addTuples(n, slope)
                if anti1[0] >= 0 and anti1[0] < boardSize[0] and anti1[1] >= 0 and anti1[1] < boardSize[1] and anti1 not in antis:
                    antis.append(anti1)
                if anti2[0] >= 0 and anti2[0] < boardSize[0] and anti2[1] >= 0 and anti2[1] < boardSize[1] and anti2 not in antis:
                    antis.append(anti2)
                    
    return len(antis)

def tryAddNode(nodes : list, node : tuple, boardSize : tuple) -> bool:
    if node[0] >= 0 and node[0] < boardSize[0] and node[1] >= 0 and node[1] < boardSize[1]:
        if node not in nodes:
            nodes.append(node)
        return True
    return False
        
def getPart2(input : list) -> int:
    symbols = findSymbols(input)
    boardSize = (len(input[0]), len(input)) # (width, height)
    antis = []
    for k in symbols.keys():
        while len(symbols[k]) > 0:
            node = symbols[k].pop(0)
            for n in symbols[k]:
                tryAddNode(antis, node, boardSize)
                tryAddNode(antis, n, boardSize)
                slope = subTuples(n, node)
                curr = node
                while True:
                    curr = subTuples(curr, slope)
                    if not tryAddNode(antis, curr, boardSize):
                        break
                curr = n
                while True:
                    curr = addTuples(curr, slope)
                    if not tryAddNode(antis, curr, boardSize):
                        break
    return len(antis)

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2


    answer[0] = getPart1(input)
    answer[1] = getPart2(input)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
