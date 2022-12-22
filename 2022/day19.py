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

class Blueprint:
    def __init__(self, data) -> None:
        self.id = data.split(':')[0].split(' ')[1]
        bots = data.split(': ')[1].split('. ')
        self.costs = {}
        self.costs['ore'] = {'ore':int(bots[0].split(' ')[4])}
        self.costs['clay'] = {'ore':int(bots[1].split(' ')[4])}
        self.costs['obsidian'] = {'ore':int(bots[2].split(' ')[4]), 'clay':int(bots[2].split(' ')[7])}
        self.costs['geode'] = {'ore':int(bots[3].split(' ')[4]), 'obsidian':int(bots[3].split(' ')[7])}

def initInventory():
    robots = {'ore':1,'clay':0,'obsidian':0,'geode':0}
    inventory = {'ore':0,'clay':0,'obsidian':0,'geode':0}
    return robots, inventory

def getAnswer(input, isSample):
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    blueprints = {}
    for l in input:
        b = Blueprint(l)
        blueprints[b.id] = b
    
    for b in blueprints.values():
        robots, inventory = initInventory()
        for m in range(25):
            new_robots = {}
            if inventory['obsidian'] >= b.costs['geode']['obsidian'] and inventory['ore'] >= b.costs['geode']['ore']:
                new_robots['geode'] = 1
                inventory['obsidian'] -= b.costs['geode']['obsidian']
                inventory['ore'] -= b.costs['geode']['ore']
            if inventory['clay'] >= b.costs['obsidian']['clay'] and inventory['ore'] >= b.costs['obsidian']['ore']:
                new_robots['obsidian'] = 1
                inventory['clay'] -= b.costs['obsidian']['clay']
                inventory['ore'] -= b.costs['obsidian']['ore']
            if inventory['ore'] >= b.costs['clay']['ore']:
                new_robots['clay'] = 1
                inventory['ore'] -= b.costs['clay']['ore']
            if inventory['ore'] >= b.costs['ore']['ore']:
                new_robots['ore'] = 1
                inventory['ore'] -= b.costs['ore']['ore']

            for r in robots.keys():
                inventory[r] += robots[r]
            for r in new_robots.keys():
                robots[r] += 1
        print('Blueprint {}:\nInventory:\n{}\nRobots:\n{}'.format(b.id, inventory, robots))
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
