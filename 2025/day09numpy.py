from ..Libraries.AdventOfCode import menu
from operator import itemgetter
import re
import numpy as np

EMPTY_TILE = 0
RED_TILE = 2
GREEN_TILE = 1

def getArea(n1 : tuple, n2 : tuple) -> int:
    height = abs(n1[1] - n2[1]) + 1
    width = abs(n1[0] - n2[0]) + 1
    return height * width

def getConnections(nodes : list) -> dict:
    connections = {}
    for n1 in nodes:
        for n2 in nodes:
            if n1 == n2: continue
            if (n2, n1) in connections.keys(): continue
            connections[(n1, n2)] = getArea(n1, n2)
    return dict(sorted(connections.items(), key=lambda item: item[1], reverse=True))

def getPart1(nodes : list) -> int:
    connections = getConnections(nodes)
    return list(connections.values())[0]

def printMap(nodeMap : list):
    for r in range(len(nodeMap)):
        line = ""
        for c in range(len(nodeMap[0])):
            line += nodeMap[r][c]
        print(line)

def findFirstNonMatching(s, value_to_match):
    index = next((i for i, x in enumerate(s) if x != value_to_match), None)
    return index

def findLastNonMatching(s, pattern):
    match = re.search(fr'.*({pattern})', s)
    if match:
        return match.end(1) - 1
    return None

def connectNodes(nodeMap : list, n1 : tuple, n2 : tuple):
    if n1[0] == n2[0]:
        # same col, fill in rows
        start_row = min(n1[1], n2[1]) + 1 # start on the next row after the lowest row node
        end_row = max(n1[1], n2[1]) # end on the row before the highest row node (due to range being -1)
        for r in range(start_row, end_row):
            if nodeMap[r][n1[0]] == EMPTY_TILE:
                nodeMap[r][n1[0]] = GREEN_TILE
        return
    if n1[1] == n2[1]:
        # same row, fill in cols
        start_col = min(n1[0], n2[0]) + 1 # start on the next col after the lowest col node
        end_col = max(n1[0], n2[0]) # end on the col before the highest col node (due to range being -1)
        row = nodeMap[n1[1]]
        nodeMap[n1[1]] = list(row[0:start_col] + [GREEN_TILE for x in range(end_col-start_col+1)] + row[end_col+1:])
        return

def getMap(nodes : list) -> list:
    # get max row and max col to know how large the map has to be
    print('1/5: get max row, col')
    max_row = max(nodes, key=itemgetter(1))[1]+1
    max_col = max(nodes, key=itemgetter(0))[0]+1
    print(f'max row, col = {max_row}, {max_col}\n2/5: initialize nodeMap')
    nodeMap = [[EMPTY_TILE for _ in range(max_col)] for _ in range(max_row)] #np.zeros((max_row, max_col))
    print('3/5: add red tiles')
    for n in nodes:
        nodeMap[n[1]][n[0]] = RED_TILE
    
    print('4/5: connectNodes')
    for n in range(len(nodes)-1):
        connectNodes(nodeMap, nodes[n], nodes[n+1])
    connectNodes(nodeMap, nodes[0], nodes[-1])
    
    print('5/5: fill in green tiles')
    for r in range(len(nodeMap)):
        row = "".join(nodeMap[r])
        start = findFirstNonMatching(row, 0)
        if start is None: continue
        end = findLastNonMatching(row, 0)
        if end is None: continue
        temp = row[0:start-1] + row[start:end].replace(EMPTY_TILE, GREEN_TILE) + row[end+1:]
        nodeMap[r] = list(temp)
        
    return nodeMap

def isValidArea(nodeMap : list, n1 : tuple, n2 : tuple) -> bool:
    x1 = min(n1[0], n2[0])
    x2 = max(n1[0], n2[0])+1
    y1 = min(n1[1], n2[1])
    y2 = max(n1[1], n2[1])+1
    for r in range(y1, y2):
        if 0 in nodeMap[r][x1:x2]: return False
    return True

def getMaxArea(nodeMap : list, connections : dict) -> int:
    #maxArea = 0
    print(f'connection count = {len(connections.keys())}')
    for k in connections.keys():
        if isValidArea(nodeMap, k[0], k[1]):# and connections[k] > maxArea: 
            return connections[k] # because connections are sorted desc by area, should be able to just find first valid one
            #maxArea = connections[k]
            #print(f'maxArea now for {k} = {connections[k]}')
    return 0

def getPart2(nodes : list) -> int:
    print('Call getMap')
    nodeMap = getMap(nodes)
    print('getMap done, call getConnections')
    connections = getConnections(nodes)
    print('getConnections done, call getMaxArea')
    return getMaxArea(nodeMap, connections)

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    input = [tuple(map(int,l.split(','))) for l in input]
    #answer[0] = getPart1(input)
    answer[1] = getPart2(input)
    return answer

while(True):
    ans = getAnswer(*menu("/2025/day09.py"))
    print('\nanswer: {}'.format(ans))
