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
    if not os.getcwd().endswith('2025'): os.chdir('2025')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2025'): os.chdir('2025')
    f = open(path, 'w')
    f.write(s)
    f.close()

def itemInRange(item : int, start : int, end : int) -> bool:
    return item >= start and item <= end

def getPart1(input : list) -> int:
    numFresh = 0
    items = [int(i) for i in input[1].split("\n")]
    ranges = [(int(start), int(end)) for start, end in [line.split("-") for line in input[0].split("\n")]]
    for item in items:
        for r in ranges:
            if itemInRange(item, r[0], r[1]):
                numFresh += 1
                break
            
    return numFresh

def getPart2(input : list) -> int:
    ranges = [(int(start), int(end)) for start, end in [line.split("-") for line in input[0].split("\n")]]
    ranges.sort()
    freshIDs = [ranges[0]]

    for curr_start, curr_end in ranges[1:]:
        last_merged_end = freshIDs[-1][1]
        if curr_start <= last_merged_end:
            freshIDs[-1] = (freshIDs[-1][0], max(last_merged_end, curr_end))
        else:
            freshIDs.append((curr_start, curr_end))

    freshCount = 0
    for f in freshIDs:
        freshCount += f[1]-f[0]+1

    return freshCount

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n\n") # split fresh from available
    answer = [0,0] #part1, part2


    answer[0] = getPart1(input)
    answer[1] = getPart2(input)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
