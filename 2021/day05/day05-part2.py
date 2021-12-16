BOARD_SIZE = 1000

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Point):
            return (self.x == other.x) and (self.y == other.y)
        return False

    def copy(self):
        return Point(self.x, self.y)

class Vent:
    def __init__(self, data):
        self.data = data
        temp = data.split(' -> ')
        self.start = temp[0].split(',')
        self.start = Point(int(self.start[0]), int(self.start[1]))
        self.end = temp[1].split(',')
        self.end = Point(int(self.end[0]), int(self.end[1]))

        self.points = []
        self.points.append(self.start)
        
        curr = self.start.copy()
        while not (curr == self.end):
            if curr.x < self.end.x:
                curr.x += 1
            elif curr.x > self.end.x:
                curr.x -= 1
            if curr.y < self.end.y:
                curr.y += 1
            elif curr.y > self.end.y:
                curr.y -= 1
                
            self.points.append(curr)
            curr = curr.copy()

        #self.points.append(self.end)

    def print(self):
        print("Start/End: {}/{}\nPoints:".format(self.start, self.end))
        for i in range(len(self.points)):
            print(self.points[i])

def printBoard(b):
    for i in range(BOARD_SIZE):
        line = ""
        for j in range(BOARD_SIZE):
            line += str(b[i][j])
        print(line)


f = open("input.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

board = [[0 for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]

vents = []
for d in data:
    v = Vent(d)
    if len(v.points) > 1:
        vents.append(v)

#vents[0].print()

for v in vents:
    for p in v.points:
        x = p.x
        y = p.y
        board[x][y] += 1

count = 0
for i in range(BOARD_SIZE):
    line = ""
    for j in range(BOARD_SIZE):
        if board[j][i] == 0:
            line += "."
        else:
            line += str(board[j][i])
        if board[j][i] > 1:
            count += 1
    #print(line)
print(count)