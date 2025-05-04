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

def swapPos(passwd : str, cmd : str) -> str:
    cSplit = cmd.split(" ")
    x = int(cSplit[2])
    y = int(cSplit[-1])

    xLetter = passwd[x]
    pList = list(passwd)
    pList[x] = pList[y]
    pList[y] = xLetter
    return "".join(pList)

def swapLetter(passwd : str, cmd : str) -> str:
    cSplit = cmd.split(" ")
    x = cSplit[2]
    y = cSplit[-1]
    return passwd.replace(x, "*").replace(y, x).replace("*", y)

def rotate(passwd : str, cmd : str) -> str:
    cSplit = cmd.split(" ")
    x = int(cSplit[2]) % len(passwd)
    scrambled = passwd
    for _ in range(x):
        if cSplit[1] == "left":
            scrambled = scrambled[1:] + scrambled[0]
        else:
            scrambled = scrambled[-1] + scrambled[:len(scrambled)-1]
    return scrambled

def rotatePos(passwd : str, cmd : str) -> str:
    letter = cmd.split(" ")[-1]
    pos = passwd.find(letter)
    add = 2 if pos >= 4 else 1
    scrambled = passwd
    for _ in range(pos + add):
        scrambled = scrambled[-1] + scrambled[:len(scrambled)-1]
    return scrambled

def reversePos(passwd : str, cmd : str) -> str:
    cSplit = cmd.split(" ")
    x = int(cSplit[2])
    y = int(cSplit[-1])
    sub = passwd[x:y+1][::-1]
    scrambled = passwd
    if x > 0:
        if y == len(passwd)-1:
            scrambled = passwd[:x] + sub
        else:
            scrambled = passwd[:x] + sub + passwd[y+1:]
    else:
        if y == len(passwd)-1:
            scrambled = sub
        else:
            scrambled = sub + passwd[y+1:]
    return scrambled

def movePos(passwd : str, cmd : str) -> str:
    cSplit = cmd.split(" ")
    x = int(cSplit[2])
    y = int(cSplit[-1])
    pList = list(passwd)
    xLetter = pList.pop(x)
    if y > len(pList): y = len(pList)
    pList.insert(y, xLetter)
    return "".join(pList)

def execCmd(passwd : str, cmd : str) -> str:
    if cmd.startswith("swap position"): return swapPos(passwd, cmd)
    if cmd.startswith("swap letter"): return swapLetter(passwd, cmd)
    if cmd.startswith("rotate based"): return rotatePos(passwd, cmd)
    if cmd.startswith("rotate"): return rotate(passwd, cmd)
    if cmd.startswith("reverse"): return reversePos(passwd, cmd)
    if cmd.startswith("move"): return movePos(passwd, cmd)
    print(f"Unknown cmd: {cmd}")
    return passwd # fallback

def getPart1(input : list, passwd : str) -> str:
    scrambled = passwd
    for line in input:
        scrambled = execCmd(scrambled, line)

    return scrambled

def getPart2(input : list, passwd : str) -> str:
    return 0

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    passwd = "abcdefgh"
    if isSample:
        passwd = "abcde"

    answer[0] = getPart1(input, passwd)
    answer[1] = getPart2(input, "fbgdceah")
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
