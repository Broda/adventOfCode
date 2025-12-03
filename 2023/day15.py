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
    if not os.getcwd().endswith('2023'): os.chdir('2023')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2023'): os.chdir('2023')
    f = open(path, 'w')
    f.write(s)
    f.close()

def hash(s) -> int:
    currVal = 0
    for c in s:
        currVal += ord(c)
        currVal *= 17
        currVal %= 256
    return currVal

boxes = {}

def processSequence(steps):
    for s in steps:
        processStep(s)
    
    sum = 0
    for k in boxes.keys():
        for i in range(len(boxes[k])):
            power = (1+k) * (1+i) * boxes[k][i][1]
            print(f'{boxes[k][i][0]} = {power}')
            sum += power
    return sum

def processStep(step):
    if '=' in step:
        lens = step.split('=')
        lens[1] = int(lens[1])
        box = hash(lens[0])
        if box in boxes.keys():
            updated = False
            for b in range(len(boxes[box])):
                if boxes[box][b][0] == lens[0]:
                    boxes[box][b][1] = lens[1]
                    updated = True
                    break
            if not updated:
                boxes[box].append(lens)
        else:
            boxes[box] = [lens]
    else: #-
        lens = step[:-1]
        box = hash(lens)
        if box in boxes.keys():
            for b in range(len(boxes[box])):
                if boxes[box][b][0] == lens:
                    boxes[box].pop(b)
                    break


def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    #print(hash('HASH'))

    steps = input[0].split(',')
    sum = 0
    for step in steps:
        sum += hash(step)

    answer[0] = sum
    answer[1] = processSequence(steps)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))


