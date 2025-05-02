import os
import sys
import hashlib

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

def getPart1(input : str) -> int:
    passwd = ""
    index = 0
    while len(passwd) < 8:
        doorID = input + str(index)
        currHash = hashlib.md5(doorID.encode('utf-8')).hexdigest()
        if currHash[0:5] == "00000":
            passwd += currHash[5]
            print(f'index: {index}, currHash: {currHash}, passwd: {passwd}')
        index += 1
    return passwd

def getPart2(input : str) -> int:
    passwd = [" "] * 8
    index = 0
    while " " in passwd:
        doorID = input + str(index)
        currHash = hashlib.md5(doorID.encode('utf-8')).hexdigest()
        if currHash[0:5] == "00000":
            if currHash[5].isdigit():
                pos = int(currHash[5])
                if pos >= 0 and pos <= 7:
                    if passwd[pos] == " ":
                        passwd[pos] = currHash[6]
                        print(f'index: {index}, currHash: {currHash}, passwd: {"".join(passwd)}')
        index += 1
    return "".join(passwd)

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")[0]
    answer = [0,0] #part1, part2


    answer[0] = getPart1(input)
    answer[1] = getPart2(input)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
