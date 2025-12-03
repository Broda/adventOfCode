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

def getPart1(list1, list2) -> int:
    dist = 0

    for i in range(len(list1)):
        dist += abs(list1[i] - list2[i])

    return dist

def getPart2(list1, list2) -> int:
    score = 0

    for num in list1:
        score += num * list2.count(num)

    return score

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    list1, list2 = [], []
    for l in input:
        list1.append(int(l.split()[0]))
        list2.append(int(l.split()[1]))
    
    list1.sort(), list2.sort()
    answer[0] = getPart1(list1, list2)
    answer[1] = getPart2(list1, list2)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))


