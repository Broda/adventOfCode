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

class Item:
    def __init__(self, itemStr : str):
        self.name, self.type = itemStr.replace(" and", "").replace(",", "").replace(".","").split(" ")
        
        if self.type == "microchip":
            self.name = self.name.replace("-compatible", "")
            self.type = "M"
        else:
            self.type = "G"

    def isSafe(self, floor : list) -> bool:
        i : Item

        for i in floor:
            if self == i: continue # skip this item
            if self.type == "M" and i.type == "G" and self.name == i.name: return True # if generator for this type of chip is on floor, it's safe
            if self.type == "G" and i.type == "M" and self.name == i.name: return True # if chip for this type of generator is on floor, it's safe

        for i in floor:
            if self == i: continue # skip this item
            if self.type == "M" and i.type == "G": return False # if no generator for this type of chip, not safe

        return True
    
    def __eq__(self, item) -> bool:
        return self.type == item.type and self.name == item.name
    
    def __str__(self) -> str:
        return f"{self.name} {self.type}"
    
    def __repr__(self) -> str:
        return f"{self.name} {self.type}"

def getGeneratorsOnFloor(floor : list) -> list:
    gens : list = []
    i : Item
    for i in floor:
        if i.type == "G": gens.append(i)
    return gens

def getChipsOnFloor(floor : list) -> list:
    chips : list = []
    i : Item
    for i in floor:
        if i.type == "M": chips.append(i)
    return chips

def getPart1(input : list) -> int:
    floors : dict = {1 : [], 2 : [], 3 : [], 4 : []}
    index : int = 1
    for line in input:
        lSplit = line.split(" contains")[1].split(" a ")
        
        for i in lSplit:
            if len(i) > 0:
                floors[index].append(Item(i))

        index += 1
        if index == 4: break

    
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
