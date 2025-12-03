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

def getPart1(input : list) -> int:
    msg = ""
    msglen = len(input[0])
    for i in range(msglen):
        d = {}
        currMaxChar = ""
        currMax = -1
        for j in range(len(input)):
            currChar = input[j][i]
            if currChar in d:
                d[currChar] += 1
            else:
                d[currChar] = 1
            if d[currChar] > currMax:
                currMax = d[currChar]
                currMaxChar = currChar
        msg += currMaxChar
                
    return msg

def getPart2(input : list) -> int:
    msg = ""
    msglen = len(input[0])
    for i in range(msglen):
        d = {}
        currMinChar = ""
        currMin = -1
        for j in range(len(input)):
            currChar = input[j][i]
            if currChar in d:
                d[currChar] += 1
            else:
                d[currChar] = 1
        for k in d.keys():
            if currMinChar == "":
                currMinChar = k
                currMin = d[k]
            else:
                if d[k] < currMin:
                    currMinChar = k
                    currMin = d[k]
        msg += currMinChar
                
    return msg

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2


    answer[0] = getPart1(input)
    answer[1] = getPart2(input)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
