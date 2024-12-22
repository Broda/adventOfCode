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

def mix(val : int, secretNum : int) -> int:
    return val ^ secretNum

def prune(secretNum : int) -> int:
    return secretNum % 16777216

def getNextNum(secretNum : int) -> int:
    val = secretNum
    nextNum = prune(mix(val << 6, secretNum))
    val = nextNum 
    nextNum = prune(mix(val >> 5, nextNum))
    val = nextNum
    nextNum = prune(mix(val << 11, nextNum))
    return nextNum

def getNumBananas(secretNum : int) -> int:
    return secretNum % 10

def getPart1(secretNums : list, allNums : list) -> int:
    startingNums = secretNums.copy()

    for i in range(2000):
        for n in range(len(secretNums)):
            secretNums[n] = getNextNum(secretNums[n])
            allNums[n].append(secretNums[n])

    sumNums = 0
    for n in range(len(secretNums)):
        sumNums += secretNums[n]

    return sumNums

def getBananaChanges(secretNums : list) -> list:
    bananaChanges = [[secretNums[0], getNumBananas(secretNums[0]), 0]]
    maxBananas = 0
    maxBananasIndex = 0
    for n in range(1, len(secretNums)):
        bananas = getNumBananas(secretNums[n])
        bananaChanges.append([secretNums[n], bananas, bananas - bananaChanges[n-1][1]])
        if n > 3 and bananas > maxBananas:
            maxBananas = bananas
            maxBananasIndex = n
    
    seq = [bananaChanges[maxBananasIndex-3][2], bananaChanges[maxBananasIndex-2][2], bananaChanges[maxBananasIndex-1][2], bananaChanges[maxBananasIndex][2]]
    #print(maxBananas, seq)
    return seq

def getBananasFromSeq(changeList : list, seq : list) -> int:
    for n in range(len(changeList)-3):
        if changeList[n][2] == seq[0]:
            if changeList[n+1][2] == seq[1]:
                if changeList[n+2][2] == seq[2]:
                    if changeList[n+3][2] == seq[3]:
                        return changeList[n+3][1]
    return 0

def getPart2(allSecretNums : list) -> int:
    sellers = {}
    for n in allSecretNums:
        sellers[n[0]] = getBananaChanges(n)
    print(sellers)
    return 0

def getAnswer(input, isSample) -> list:
    input = [int(x) for x in input.replace("\r", "").split("\n")]
    answer = [0,0] #part1, part2

    allNums = [[x] for x in input]
    answer[0] = getPart1(input, allNums)
    answer[1] = getPart2(allNums)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
