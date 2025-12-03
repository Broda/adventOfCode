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

class Card:
    def __init__(self, line) -> None:
        self.line = line
        self.id = int(line.split(':')[0].split(' ')[-1].strip())
        self.copies = 1
        cards = line.split(':')[1].split('|')
        self.winningNumbers = set(x.strip() for x in cards[0].split())
        self.playNumbers = set(x.strip() for x in cards[1].split())
        self.wins = self.getWinCount()

    def getWinCount(self):
        wins = set(x for x in self.playNumbers if x in self.winningNumbers)
        return len(wins)
        
def getCards(input):
    cards = {}
    for l in input:
        c = Card(l)
        cards[c.id] = c
    return cards

def getPoints(cards):
    points = 0
    for c in cards.values():
        if c.wins > 0:
            points += 2 ** (c.wins-1)
    return points

def getTotalCount(cards):
    for k in range(1,len(cards)+1):
        wins = cards[k].wins
        if wins == 0: pass
        for i in range(k+1,k+wins+1):
            cards[i].copies += cards[k].copies
        print(f'{k}: {wins} wins, {cards[k].copies} copies')
    count = 0
    for c in cards.values():
        count += c.copies
    return count

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    cards = getCards(input)

    answer[0] = getPoints(cards)
    answer[1] = getTotalCount(cards)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))


