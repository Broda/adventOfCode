import sys
import os

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

cardValues = {'A':13,'K':12,'Q':11,'J':10,'T':9,'9':8,
         '8':7,'7':6,'6':5,'5':4,'4':3,'3':2,'2':1}

hands = {'five':[],'four':[],'full':[],'three':[],
         'two':[],'one':[],'high':[]}

class Hand:
    def __init__(self, line) -> None:
        self.line = line
        self.hand, self.bid = line.split()
        self.bid = int(self.bid)
        self.type = self.getType()
        self.score = self.scoreHand()

    def __str__(self) -> str:
        return f'{self.line}'
    
    def getType(self):
        cards = {}
        for c in self.hand:
            if c in cards.keys():
                cards[c] += 1
            else:
                cards[c] = 1
        #print(cards)
        found3 = False
        foundPair = False
        for k in cards.keys():
            if cards[k] == 5:
                return 'five'
            if cards[k] == 4:
                return 'four'
            if cards[k] == 3:
                found3 = True
            if cards[k] == 2:
                if foundPair:
                    return 'two'
                foundPair = True
        if found3 and foundPair:
            return 'full'
        if found3:
            return 'three'
        if foundPair:
            return 'one'
        return 'high'
    
    def scoreHand(self):
        score = 0
        score += cardValues[self.hand[0]] * 100000000
        score += cardValues[self.hand[1]] * 1000000
        score += cardValues[self.hand[2]] * 10000
        score += cardValues[self.hand[3]] * 100
        score += cardValues[self.hand[4]]
        return score
    
def parseHands(data):
    for l in data:
        h = Hand(l)
        hands[h.type].append(h)

def rankHands():
    ranks = []
    
    for k in hands.keys():
        hands[k].sort(key=lambda x: x.score, reverse=True)
    
    ranks += hands['five']
    ranks += hands['four']
    ranks += hands['full']
    ranks += hands['three']
    ranks += hands['two']
    ranks += hands['one']
    ranks += hands['high']
    return ranks


def getAnswer(data, isSample) -> list:
    data = data.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    parseHands(data)
    ranks = rankHands()
    values = []
    sum = 0
    index = 0
    for r in range(len(ranks), 0, -1):
        values.append((ranks[index], ranks[index].bid * r))
        #print(f'[{index} / {r}]: {values[-1][0]} = {values[-1][1]}')
        sum += ranks[index].bid * r
        index += 1

    answer[0] = sum
    answer[1] = 0
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))


