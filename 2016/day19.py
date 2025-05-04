import os
import sys
import math

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

def getPart1(numElves : int) -> int:
    elves = []
    for i in range(numElves):
        elves.append(i+1)
    
    while len(elves) > 1:
        newElves = []
        for i in range(0, len(elves), 2):
            newElves.append(elves[i])
        if len(elves) % 2 == 1 and len(elves) > 1:
            newElves.pop(0)
        elves = newElves

    return elves[0]

def getPart2(numElves : int) -> int:
    i = 1
    while i * 3 < numElves:
        i *= 3
    return numElves - i

    # brute force below takes WAY TOO LONG
    elves = []
    for i in range(numElves):
        elves.append(i+1)

    currElfIndex = 0
    while len(elves) > 1:
        remIndex = math.floor(len(elves) / 2) + currElfIndex
        #print(f"currElfIndex: {currElfIndex} = elf #{elves[currElfIndex]}, remIndex: {remIndex}")
        if remIndex >= len(elves): 
            #print(f"remIndex >= len(elves): {remIndex} >= {len(elves)}, remIndex %= len(elves): {remIndex % len(elves)}")
            remIndex %= len(elves)
        #print(f"removing elves[remIndex]: elf #{elves[remIndex]}")
        elves.remove(elves[remIndex])

        currElfIndex += 1
        if currElfIndex >= len(elves): currElfIndex = 0

    return elves[0]

def getAnswer(input, isSample) -> list:
    input = int(input.replace("\r", "").split("\n")[0])
    answer = [0,0] #part1, part2

    answer[0] = getPart1(input)
    answer[1] = getPart2(input)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
