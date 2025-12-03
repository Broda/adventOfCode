import sys
import os
from itertools import permutations

def readFile(path):
    if not os.getcwd().endswith('2015'): os.chdir('2015')
    f = open(path, "r")
    return f.read().strip()

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

def getHighestHappiness(people, changes):
    best = 0
    for items in permutations(people):
        happiness = 0
        for i in range(len(items)-1):
            happiness += changes[items[i]][items[i+1]]
            happiness += changes[items[i+1]][items[i]]
        happiness += changes[items[0]][items[-1]]
        happiness += changes[items[-1]][items[0]]
        
        best = max(best, happiness)
    return best

def getAnswer(input):
    if '\r' in input or '\n' in input:
        input = input.replace("\r", "").split("\n")

    answer = ['',''] #part1, part2
    
    people = set()
    changes = dict()
    for l in input:
        # Alice would gain 54 happiness units by sitting next to Bob.
        # Alice would lose 79 happiness units by sitting next to Carol.
        l = l.replace('gain ', '')
        l = l.replace('lose ', '-')
        l = l[:-1]
        # Alice would 54 happiness units by sitting next to Bob
        # Alice would -79 happiness units by sitting next to Carol
        (p1, _, units, _, _, _, _, _, _, p2) = l.split()
        people.add(p1)
        people.add(p2)
        changes.setdefault(p1, dict())[p2] = int(units)
    
    answer[0] = getHighestHappiness(people, changes)
    
    me = 'Me'
    for p in people:
        changes.setdefault(me, dict())[p] = 0
        changes.setdefault(p, dict())[me] = 0
    people.add(me)

    answer[1] = getHighestHappiness(people, changes)

    return answer

while(True):
    ans = getAnswer(menu())
    print(ans)
