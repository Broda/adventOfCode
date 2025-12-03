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

def getDragonCurve(input : str) -> str:
    b = input[::-1]
    curve = f"{input}0"
    for c in b:
        if c == "0":
            curve += "1"
        else:
            curve += "0"
    
    return curve

def getChecksum(data : str) -> str:
    chk = ""
    for i in range(0, len(data), 2):
        if data[i] == data[i+1]:
            chk += "1"
        else:
            chk += "0"
    return chk

def getPart1(input : str, length : int) -> str:
    data = input
    while len(data) < length:
        data = getDragonCurve(data)

    data = data[:length]
    chk = getChecksum(data)
    while len(chk) % 2 == 0:
        chk = getChecksum(chk)
    
    return chk

def getPart2(input : str, length : int) -> int:
    return getPart1(input, length)

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")[0]
    answer = [0,0] #part1, part2

    length = 272
    if isSample:
        length = 20

    answer[0] = getPart1(input, length)
    answer[1] = getPart2(input, 35651584)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
