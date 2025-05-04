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

def isBlocked(data : list, ip : int, maxVal : int) -> bool:
    for start, end in data:
        if start <= ip <= end:
            return False
    return ip < maxVal #2**32

def getPart1(input : list, maxVal : int) -> tuple:
    
    data = sorted([int(left), int(right)] for left,right in [line.split("-") for line in input])
    possibles = [x[1]+1 for x in data]
    valids = [p for p in possibles if isBlocked(data, p, maxVal)]

    total = 0
    for ip in valids:
        while isBlocked(data, ip, maxVal):
            total += 1
            ip += 1

    return (valids[0], total)

def getPart2() -> int:
    return 0

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    maxVal : int = 2**32
    if isSample: maxVal = 9

    answer = getPart1(input, maxVal)
    #answer[1] = getPart2()
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
