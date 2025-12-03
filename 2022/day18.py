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
    if not os.getcwd().endswith('2022'): os.chdir('2022')
    f = open(path, "r")
    return f.read().strip()

def getAnswer(input, isSample):
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    cubes = {}
    cubes_opp = {}

    for l in input:
        x, y, z = list(map(int,l.split(',')))
        cubes[(x,y,z)] = []
        cubes_opp[(x,y,z)] = []
    
    for c in cubes.keys():
        for d in cubes.keys():
            if c == d: continue
            if c[0] in [d[0]-1,d[0]+1] and c[1] == d[1] and c[2] == d[2]:
                cubes[c].append(d)
                continue
            if c[0] == d[0] and c[1] in [d[1]-1,d[1]+1] and c[2] == d[2]:
                cubes[c].append(d)
                continue
            if c[0] == d[0] and c[1] == d[1] and c[2] in [d[2]-1,d[2]+1]:
                cubes[c].append(d)
                continue
            if c[0] == d[0] and c[1] == d[1]:
                cubes_opp.append(d)
                continue
            if c[0] == d[0] and c[2] == d[2]:
                cubes_opp.append(d)
            if c[1] == d[1] and c[2] == d[2]:
                cubes_opp[c].append(d)
                continue
            
        answer[0] += 6 - len(cubes[c])

    for c in cubes.keys():
        for d in cubes_opp[c]:
            for e in cubes.keys():
                
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
