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

def rotate(curVal, amount) -> tuple:
    direction = 1 if amount[0] == 'R' else -1
    steps = int(amount[1:])
    numbers = [i for i in range(100)]
    idx = curVal
    numZeros = 0
    for i in range(steps):
        idx += direction
        if idx == 100:
            idx = 0
        if idx == -1:
            idx = 99
        if idx == 0:
            numZeros += 1
    return (idx, numZeros)

def getPart1(input : list) -> int:
    val = 50
    cnt = 0
    for line in input:
        val = rotate(val, line)[0]
        if val == 0:
            cnt += 1
    return cnt

def getPart2(input : list) -> int:
    val = 50
    totalZeros = 0

    for line in input:
        val, cnt = rotate(val, line)
        totalZeros += cnt
    return totalZeros

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2


    answer[0] = getPart1(input)
    answer[1] = getPart2(input)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
