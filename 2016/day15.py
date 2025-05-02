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
    if not os.getcwd().endswith('2016'): os.chdir('2016')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2016'): os.chdir('2016')
    f = open(path, 'w')
    f.write(s)
    f.close()

def loadDiscs(input : list) -> list:
    discs = []
    for d in input:
        dSplit = d.replace(".","").split(" ")
        discs.append([int(dSplit[3]), int(dSplit[-1])])
    return discs

def tryDrop(dropTime : int, discs : list) -> bool:
    print(f"tryDrop({dropTime})")
    for i in range(len(discs)):
        numPos, currPos = discs[i]
        currPos = (currPos + dropTime + i + 1) % numPos
        print(f"disc {i+1}: ({discs[i][1]} + {dropTime} + {i} + 1) % {numPos} = {currPos}")
        if currPos != 0: return False

    return True


def getPart1(discs : list, startDropTime : int = 0) -> int:
    dropTime = startDropTime
    while not tryDrop(dropTime, discs):
        dropTime += 1

    return dropTime

def getPart2(discs : list, startDropTime : int) -> int:
    discs.append([11, 0])

    return getPart1(discs, startDropTime)

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    discs = loadDiscs(input)
    answer[0] = getPart1(discs)
    answer[1] = getPart2(discs, answer[0]-1)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
