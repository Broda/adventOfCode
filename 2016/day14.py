import os
import sys
import hashlib
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

def genHashes(salt : str, startIndex : int, numHashes : int) -> list:
    hashes = []
    for i in range(startIndex, startIndex + numHashes + 1):
        hashes.append(getHash(salt, i))
    print(f"generated {numHashes} hashes")
    return hashes

def getHash(salt : str, index : int) -> str:
    return hashlib.md5(f"{salt}{index}".encode('utf-8')).hexdigest().lower()

def genStretchedHashes(salt : str, startIndex : int, numStretches : int, numHashes : int) -> list:
    hashes = []
    for i in range(startIndex, startIndex + numHashes + 1):
        hashes.append(getStretchedHash(salt, i, numStretches))
    print(f"generated {numHashes} stretched hashes")
    return hashes

def getStretchedHash(salt : str, index : int, numStretches : int) -> str:
    stretched = getHash(salt, index)
    for _ in range(numStretches):
        stretched = hashlib.md5(stretched.encode('utf-8')).hexdigest().lower()
    return stretched

def isKey(salt : str, index : int, hashes : list) -> bool:
    currHash = hashes[index]
    m = re.search(r"(.)\1\1", currHash)
    if m:
        char = m.group(1)
        
        for i in range(index+1, index+1001):
            if i >= len(hashes):
                hashes += genHashes(salt, i, 1000)
                
            h = hashes[i]
            if char*5 in h:
                return True
    return False

def isStretchedKey(salt : str, index : int, hashes : list, numStretches : int) -> bool:
    currHash = hashes[index]
    m = re.search(r"(.)\1\1", currHash)
    if m:
        char = m.group(1)
        
        for i in range(index+1, index+1001):
            if i >= len(hashes):
                hashes += genStretchedHashes(salt, i, numStretches, 1000)
                
            h = hashes[i]
            if char*5 in h:
                return True
    return False

def getPart1(input : str) -> int:
    hashes = genHashes(input, 0, 10000)

    keys : list = []
    index = 0
    while True:
        if isKey(input, index, hashes):
            keys.append(index)
            print(f"found a key @ index {index}")
            if len(keys) == 64:
                break
        index += 1
    return keys[-1]

def getPart2(input : str) -> int:
    hashes = genStretchedHashes(input, 0, 2016, 10000)

    keys : list = []
    index = 0
    while True:
        if isStretchedKey(input, index, hashes, 2016):
            keys.append(index)
            print(f"found a key @ index {index}")
            if len(keys) == 64:
                break
        index += 1
    return keys[-1]

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")[0]
    answer = [0,0] #part1, part2


    answer[0] = getPart1(input)
    answer[1] = getPart2(input)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
