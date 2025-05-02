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

class Bot:
    def __init__(self, num1 : int, num2 : int):
        self.number : int = None
        self.num1 = num1
        self.num2 = num2
        self.ruleStr : str = ""
        self.rules : dict = {}
        self.chips : list = []

    def parseRules(self, ruleStr : str) -> dict:
        self.number = int(ruleStr.split(" ")[1])
        rules = {"low":[], "high":[]}
        s = ruleStr.split(" and ")
        low = s[0].split(" ")
        rules["low"] = [low[-2], int(low[-1])]
        high = s[1].split(" ")
        rules["high"] = [high[-2], int(high[-1])]
        return rules

    def addChip(self, valueStr : str):
        temp = valueStr.split(" ")
        self.chips.append(int(temp[1]))

    def getChip(self, value : int):
        self.chips.append(value)

    def giveChip(self, value : int):
        self.chips.remove(value)
        
    def checkChips(self) -> bool:
        if len(self.chips) < 2: return False
        if self.num1 in self.chips and self.num2 in self.chips: return True
        return False
    
    def runRules(self, bots : dict, output : dict, checkChips : bool = False):
        if len(self.chips) < 2: return
        if checkChips and self.checkChips(): return
        low = -1
        high = -1
        if self.chips[0] < self.chips[1]:
            low = self.chips[0]
            high = self.chips[1]
        else:
            low = self.chips[1]
            high = self.chips[0]
        
        if self.rules["low"][0] == "output":
            if not self.rules["low"][1] in output: output[self.rules["low"][1]] = []
            output[self.rules["low"][1]].append(low)
            self.giveChip(low)
            if not checkChips and self.rules["low"][1] <= 2:
                print(f"bot {self.number} giving {low} to output {self.rules["low"][1]}")
            if checkChips and (low == self.num1 or low == self.num2):
                print(f"bot {self.number} giving {low} to output {self.rules["low"][1]}")
        else:
            if len(bots[self.rules["low"][1]].chips) < 2:
                bots[self.rules["low"][1]].getChip(low)
                self.giveChip(low)
                if checkChips and (low == self.num1 or low == self.num2):
                    print(f"bot {self.number} giving {low} to bot {self.rules["low"][1]}")
        if self.rules["high"][0] == "output":
            if not self.rules["high"][1] in output: output[self.rules["high"][1]] = []
            output[self.rules["high"][1]].append(high)
            self.giveChip(high)
            if not checkChips and self.rules["high"][1] <= 2:
                print(f"bot {self.number} giving {low} to output {self.rules["high"][1]}")
            if checkChips and (high == self.num1 or high == self.num2):
                print(f"bot {self.number} giving {high} to output {self.rules["high"][1]}")
        else:
            if len(bots[self.rules["high"][1]].chips) < 2:
                bots[self.rules["high"][1]].getChip(high)
                self.giveChip(high)
                if checkChips and (high == self.num1 or high == self.num2):
                    print(f"bot {self.number} giving {high} to bot {self.rules["high"][1]}")
        
    def __eq__(self, value : int):
        return self.number == value

    def __repr__(self):
        return f"bot {self.number}, low: {self.rules["low"]}, high: {self.rules["high"]}, has: {self.chips}"
    
    def __str__(self):
        return f"bot {self.number}, low: {self.rules["low"]}, high: {self.rules["high"]}, has: {self.chips}"
    
class BotManager :
    def __init__(self, cmds : list, num1 : int, num2 : int):
        self.bots = {}
        self.output = {}
        self.cmds = cmds
        self.loadBots(num1, num2)
    
    def loadBots(self, num1 : int, num2 : int):
        c : str
        for c in self.cmds:
            cSplit = c.split(" ")
            if c.startswith("bot"):
                num = int(cSplit[1])
                if not num in self.bots.keys():
                    self.bots[num] = Bot(num1, num2)

                self.bots[num].ruleStr = c
                self.bots[num].rules = self.bots[num].parseRules(c)
            else:
                num = int(cSplit[-1])
                if not num in self.bots.keys():
                    self.bots[num] = Bot(num1, num2)
                self.bots[num].addChip(c)
                
    def runBots(self) -> int:
        while True:
            for b in self.bots:
                if self.bots[b].checkChips(): return b
            for b in self.bots:
                self.bots[b].runRules(self.bots, self.output, True)

    def runBots2(self) -> int:
        if not 0 in self.output.keys(): self.output[0] = []
        if not 1 in self.output.keys(): self.output[1] = []
        if not 2 in self.output.keys(): self.output[2] = []
        while len(self.output[0]) == 0 or len(self.output[1]) == 0 or len(self.output[2]) == 0:
            for b in self.bots:
                self.bots[b].runRules(self.bots, self.output, False)
        return self.output[0][0] * self.output[1][0] * self.output[2][0]

    def printBots(self):
        for b in self.bots:
            print(self.bots[b])

def getPart1(input : list, num1 : int, num2 : int) -> int:
    Mgr = BotManager(input, num1, num2)

    return Mgr.runBots()

def getPart2(input : list, num1 : int, num2 : int) -> int:
    Mgr = BotManager(input, num1, num2)

    return Mgr.runBots2()

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    num1 = 61
    num2 = 17

    if isSample:
        num1 = 5
        num2 = 2

    answer[0] = getPart1(input, num1, num2)
    answer[1] = getPart2(input, num1, num2)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
