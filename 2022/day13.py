import os
import sys
from functools import cmp_to_key

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
            return readFile(samplePath)
        case "2":
            return readFile(inputPath)
        case "3":
            return readFile(input("File Name: "))
        case "4":
            return input("Input: ")
        case _:
            print("Invalid option. Try Again.\n")
            return menu()

def readFile(path):
    if not os.getcwd().endswith('2022'): os.chdir('2022')
    f = open(path, "r")
    return f.read().strip()

def comparePackets(p1, p2):
    result = 0
    p1IsList = type(p1) is list
    p2IsList = type(p2) is list
    if not p1IsList and not p2IsList:
        return (p1 > p2) - (p1 < p2)
    if not p1IsList: p1 = [p1]
    if not p2IsList: p2 = [p2]
    for i in range(min(len(p1), len(p2))):
        result = comparePackets(p1[i], p2[i])
        if result:
            return result
    
    return (len(p1) > len(p2)) - (len(p1) < len(p2))

def getAnswer(input):
    input = input.replace("\r", "").split("\n\n")
    answer = [0,0] #part1, part2

    packets = []
    for msgIndex in range(len(input)):
        packet1, packet2 = input[msgIndex].split('\n')
        packet1 = eval(packet1)
        packet2 = eval(packet2)
        packets.append(packet1)
        packets.append(packet2)
        if comparePackets(packet1, packet2) < 0: answer[0] += msgIndex+1
        
    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=cmp_to_key(comparePackets))
    answer[1] = 1
    for p in range(len(packets)):
        if packets[p] == [[2]] or packets[p] == [[6]]:
            answer[1] *= (p+1)

    return answer

while(True):
    ans = getAnswer(menu())
    print('\nanswer: {}'.format(ans))
