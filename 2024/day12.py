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

def findRegionStart(data : list) -> tuple:
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] != '.':
                return (r, c)
    return (-1, -1) # no more

def tryAddNeighbor(data : list, regions : dict, region_start : tuple, node_type : str, new_node : tuple) -> bool:
    if data[new_node[0]][new_node[1]] == node_type:
        if new_node not in regions[region_start]:
            regions[region_start].append(new_node)
            addNeighbors(data, regions, region_start, new_node)
            return True
    return False

def addNeighbors(data : list, regions : dict, region_start : tuple, curr_node : tuple) -> None:
    node_type = data[curr_node[0]][curr_node[1]] # grab letter designator
    up = curr_node[0] - 1
    down = curr_node[0] + 1
    left = curr_node[1] - 1
    right = curr_node[1] + 1
    if up >= 0:
        tryAddNeighbor(data, regions, region_start, node_type, (up, curr_node[1]))
    if down < len(data):
        tryAddNeighbor(data, regions, region_start, node_type, (down, curr_node[1]))
    if left >= 0:
        tryAddNeighbor(data, regions, region_start, node_type, (curr_node[0], left))
    if right < len(data[0]):
        tryAddNeighbor(data, regions, region_start, node_type, (curr_node[0], right))
    data[curr_node[0]][curr_node[1]] = "."

def getRegionNodePerimeter(region : list, node : tuple) -> int:
    perimeter = 4
    if (node[0]-1, node[1]) in region:
        perimeter -= 1
    if (node[0]+1, node[1]) in region:
        perimeter -= 1
    if (node[0], node[1]-1) in region:
        perimeter -= 1
    if (node[0], node[1]+1) in region:
        perimeter -= 1
    return perimeter

def getRegionPerimeter(region : list) -> int:
    sum = 0
    for n in region:
        sum += getRegionNodePerimeter(region, n)
    return sum

def getRegionPrice(region : list) -> int:
    return getRegionPerimeter(region) * len(region)


def getFences(region : list) -> list:
    fences = []
    for node in region:
        neighbor = (node[0]-1, node[1])
        if neighbor not in region: fences.append(neighbor)
        neighbor = (node[0]+1, node[1])
        if neighbor not in region: fences.append(neighbor)
        neighbor = (node[0], node[1]-1)
        if neighbor not in region: fences.append(neighbor)
        neighbor = (node[0], node[1]+1)
        if neighbor not in region: fences.append(neighbor)
    return fences

def getRegionBulkPerimeter(region : list) -> int:
    sum = 0
    
    fences = getFences(region)
    sum = len(fences)
    rows, cols = zip(*fences)
    minRows, maxRows = min(rows), max(rows)
    minCols, maxCols = min(cols), max(cols)
    horizFences = []
    vertFences = []
    for row in range(minRows, maxRows+1):
        startRow = False
        newRow = []
        for col in range(minCols, maxCols+1):
            if (row, col) in fences:
                if startRow:
                    sum -= 1
                    newRow.append((row,col))
                else:
                    startRow = True
                    newRow = [(row,col)]
            else:
                if startRow:
                    horizFences.append(newRow)
                startRow = False
                newRow = []

    for col in range(minCols, maxCols+1):
        startCol = False
        newCol = []
        for row in range(minRows, maxRows+1):
            if (row, col) in fences:
                if startCol:
                    sum -= 1
                    newCol.append((row,col))
                else:
                    startCol = True
                    newCol = [(row,col)]
            else:
                if startCol:
                    vertFences.append(newCol)
                startCol = False
                newCol = []
    
    print(f"horizontal fences [{len(horizFences)}]: {horizFences}")
    print(f"vertical fences [{len(vertFences)}]: {vertFences}")
    
    return sum

def getRegionBulkPrice(region : list) -> int:
    return getRegionBulkPerimeter(region) * len(region)

def findRegions(input : list) -> dict:
    regions = {}
    curr_node = findRegionStart(input)

    while curr_node != (-1, -1):
        regions[curr_node] = [curr_node]
        addNeighbors(input, regions, curr_node, curr_node)

        curr_node = findRegionStart(input)
    return regions

def getPart1(regions : dict) -> int:
    price = 0
    for k in regions.keys():
        price += getRegionPrice(regions[k])
    return price

def getPart2(regions : dict) -> int:
    price = 0
    for k in regions.keys():
        price += getRegionBulkPrice(regions[k])
    return price

def getAnswer(input, isSample) -> list:
    input = [list(x) for x in input.replace("\r", "").split("\n")]
    answer = [0,0] #part1, part2

    regions = findRegions(input)
    answer[0] = getPart1(regions)
    answer[1] = getPart2(regions)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
