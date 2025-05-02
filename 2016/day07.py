import os
import sys
import re

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
    cnt = 0
    for ip in input:
        m = re.search(r"[\[][a-z]*(([a-z])([a-z])\3\2)[a-z]*[\]]", ip)
        if m:
            #print('inside brackets, skip')
            continue
        m = re.search(r"(([a-z])([a-z])\3\2)", ip)
        if not m:
            #print('no match, skip')
            continue
        if m.group(2) == m.group(3):
            #print('same chars, skip')
            continue
        cnt += 1
        #print(f"ip: {ip}, m: {m}, cnt: {cnt}")
    return cnt

def getPart2(input : list) -> int:
    cnt = 0
    for ip in input:
        m = re.search(r"[\[][a-z]*(([a-z])([a-z])\2)[a-z]*[\]]", ip)
        if not m:
            continue
        rev = m.group(3) + m.group(2) + m.group(3)
        m = re.findall(r"([\[][a-z^\[]*[\]])", ip)
        tempIP = ip
        if m:
            print(m)
        for g in m:
            print(f"removing {g}")
            tempIP = tempIP.replace(g, "")
        print(f"tempIP = {tempIP}")
        m = re.search(r"(" + rev + ")", tempIP)
        if m:
            cnt += 1
            print(f"ip: {ip}, m: {m.group(1)}, cnt: {cnt}")
    return cnt

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2


    answer[0] = getPart1(input)
    answer[1] = getPart2(input)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
