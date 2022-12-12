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

def getAnswer(input):
    answer = [0,0] #part1, part2

    input = input.replace("\r", "").split("\n")
    # input format:
    # PlaceA to PlaceB = 464
    # PlaceA to PlaceC = 518
    # PlaceB to PlaceC = 141

    places = set()
    distances = dict()
    for l in input:
        (source, _, dest, _, distance) = l.split()
        places.add(source)
        places.add(dest)
        distances.setdefault(source, dict())[dest] = int(distance)
        distances.setdefault(dest, dict())[source] = int(distance)
    
    shortest = sys.maxsize
    longest = 0
    for items in permutations(places):
        dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
        shortest = min(shortest, dist)
        longest = max(longest, dist)
    
    answer[0] = shortest
    answer[1] = longest
    
    return answer

while(True):
    ans = getAnswer(menu())
    print('\nanswer: {}'.format(ans))
