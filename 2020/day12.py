import sys
import os
import re

FACES = {'E':[1,0],'S':[0,-1],'W':[-1,0],'N':[0,1]}
FACES_LIST = ['E','S','W','N']

def readFile(path):
    if not os.getcwd().endswith('2020'): os.chdir('2020')
    f = open(path, "r")
    return f.read().strip()

def printGrid(g, rev=False):
    if rev:
        for r in reversed(g):
            print(''.join(r))
    else:
        for r in g:
            print(''.join(r))

def addVector(a, b):
    v = []
    for i in range(len(a)):
        v.append(a[i] + b[i])
    return v

def subVector(a, b):
    v = []
    for i in range(len(a)):
        v.append(a[i] - b[i])
    return v

def scalarMultiplyVector(v, s):
    newV = []
    for n in v:
        newV.append(n * s)
    return newV

def menu(samplePath, inputPath):
    main = "\nPlease choose an input option:\n"
    main += "1. Sample File\n"
    main += "2. Input File\n"
    main += "3. Other File\n"
    main += "4. Prompt\n"
    main += "5. Quit\n"
    main += ">> "
    
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

def rotate(currFace, amt):
    newFace = currFace

    while amt != 0:
        index = FACES_LIST.index(newFace)
        if amt < 0:
            index -= 1
            newFace = FACES_LIST[index]
            amt += 90
        else:
            index += 1
            if index >= len(FACES_LIST): index = 0
            newFace = FACES_LIST[index]
            amt -= 90

    return newFace

def rotateWP(wp, amt):
    newWP = wp
    
    return newWP

def moveShip(currPos, currFace, cmd):
    c = cmd[0]
    amt = int(cmd[1:])
    newPos = currPos
    newFace = currFace
    match c:
        case "N":
            newPos = addVector(currPos, [0,amt])
        case "S":
            newPos = addVector(currPos, [0,-amt])
        case "E":
            newPos = addVector(currPos, [amt,0])
        case "W":
            newPos = addVector(currPos, [-amt,0])
        case "L":
            newFace = rotate(currFace, -amt)
        case "R":
            newFace = rotate(currFace, amt)
        case "F":
            newPos = addVector(currPos, scalarMultiplyVector(FACES[currFace], amt))

    return newPos, newFace

def moveShip2(currPos, wp, cmd):
    c = cmd[0]
    amt = int(cmd[1:])
    newPos = currPos
    newWP = wp
    match c:
        case "N":
            newWP = addVector(wp, [0,amt])
        case "S":
            newWP = addVector(wp, [0,-amt])
        case "E":
            newWP = addVector(wp, [amt,0])
        case "W":
            newWP = addVector(wp, [-amt,0])
        case "L":
            newWP = rotateWP(wp, -amt)
        case "R":
            newWP = rotateWP(wp, amt)
        case "F":
            for n in range(amt):
                newPos = addVector(currPos, wp)
                newWP = addVector(wp,wp)
    return newPos, newWP

def getAnswer(input):
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    CurrPos = [0,0]
    CurrFace = 'E'
    WP = [10,1]

    for l in input:
        CurrPos, CurrFace = moveShip(CurrPos, CurrFace, l)
    answer[0] = abs(CurrPos[0]) + abs(CurrPos[1])

    CurrPos = [0,0]
    WP = [10,1]

    for l in input:
        CurrPos, WP = moveShip2(CurrPos, WP, l)

    answer[1] = abs(CurrPos[0]) + abs(CurrPos[1])

    return answer

while(True):
    ans = getAnswer(menu('day12sample.txt','day12input.txt'))
    print('\nanswer: {}'.format(ans))
