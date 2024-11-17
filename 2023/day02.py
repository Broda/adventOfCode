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

class Game:
    def __init__(self, line) -> None:
        self.id = int(line.split(':')[0].split(' ')[1])
        self.pulls = line.split(':')[1].strip().split(';')
        self.maxes = {'blue':0, 'red':0, 'green':0}
        for p in self.pulls:
            cubes = p.split(', ')
            for c in cubes:
                num, color = c.strip().split(' ')
                num = int(num)
                if num > self.maxes[color]:
                    self.maxes[color] = num
    
    def isPossible(self, maxR, maxG, maxB):
        if self.maxes['red'] > maxR: return False
        if self.maxes['green'] > maxG: return False
        if self.maxes['blue'] > maxB: return False
        return True
    
    def getPower(self):
        return self.maxes['red'] * self.maxes['green'] * self.maxes['blue']

def getPossibleGames(lines, R, G, B):
    sum = 0
    for l in lines:
        g = Game(l)
        if g.isPossible(R, G, B): sum += g.id
    return sum

def getSumOfPowers(lines):
    sum = 0
    for l in lines:
        g = Game(l)
        sum += g.getPower()
    return sum

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    answer[0] = getPossibleGames(input, 12, 13, 14)
    answer[1] = getSumOfPowers(input)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))


