class Player:
    def __init__(self, data):
        self.data = data
        self.id = int(data.split(' ')[1])
        self.pos = int(data.split(' ')[-1])
        self.score = 0

    def move(self, spaces):
        #print(f'Player {self.id} moving {spaces} spaces from {self.pos}')
        self.pos = (self.pos + spaces - 1) % 10 + 1        
        self.score += self.pos
        #print(f'Player {self.id} ended on space {self.pos}. Score = {self.score}')
        return
#part 1
def rollDie(d):
    if d + 1 > 100:
        return 1
    return d + 1

def rollDice(d):
    d = rollDie(d)
    moves = d
    d = rollDie(d)
    moves += d
    d = rollDie(d)
    moves += d
    return (d,moves)

f = open("sample.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

p1 = Player(data[0])
p2 = Player(data[1])

die = 0
rolls = 0
while True:
    die, moves = rollDice(die)
    p1.move(moves)
    rolls += 3
    if p1.score >= 1000:
        break
    die, moves = rollDice(die)
    p2.move(moves)
    rolls += 3
    if p2.score >= 1000:
        break

print(f'Player 1 scored {p1.score}')
print(f'Player 2 scored {p2.score}')
losing_score = 0
if p1.score > p2.score:
    losing_score = p2.score
else:
    losing_score = p1.score

#part1
print(f'{rolls} * {losing_score} = {rolls * losing_score}')

