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
    for line in input:
        print(f"line = '{line}'")
        data = ""
        index = 0
        for _ in range(len(line)):
            if index >= len(line):
                break
            c = line[index]
            marker = ""
            if c != "(" and c != " ":
                data += c
                index += 1
                continue
            if c == "(":
                for j in range(index, len(line)):
                    if line[j] == ")":
                        marker = line[index+1:j]
                        index = j+1
                        #print(f"found ')' @ {j}, i now {index}")
                        chars, times = [int(v) for v in marker.split("x")]
                        #print(f"chars, times = {chars}, {times}")
                        dupe = line[index:index+chars]
                        #print(f"dupe = {dupe}")
                        for _ in range(times):
                            data += dupe
                        #print(f"data = {data}")
                        index += chars
                        #print(f"i now {index}")
                        break
                
        print(data)
        print(f"len = {len(data)}")

    return 0

def getPart2(input : list) -> int:
    return 0

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2


    answer[0] = getPart1(input)
    answer[1] = getPart2(input)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
