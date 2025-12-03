class Vent:
    def __init__(self, data):
        self.data = data
        temp = data.split(' -> ')
        self.start = temp[0].split(',')
        self.start[0] = int(self.start[0])
        self.start[1] = int(self.start[1])
        self.end = temp[1].split(',')
        self.end[0] = int(self.end[0])
        self.end[1] = int(self.end[1])

        self.points = []
        self.points.append(self.start)
        if self.start[0] == self.end[0]:
            curr = self.start[1]
            if self.end[1] > self.start[1]:
                while curr < self.end[1]:
                    curr += 1
                    self.points.append([self.start[0], curr])
            else:
                while curr > self.end[1]:
                    curr -= 1
                    self.points.append([self.start[0], curr])
        elif self.start[1] == self.end[1]:
            curr = self.start[0]
            if self.end[0] > self.start[0]:
                while curr < self.end[0]:
                    curr += 1
                    self.points.append([curr, self.start[1]])
            else:
                while curr > self.end[0]:
                    curr -= 1
                    self.points.append([curr, self.start[1]])

    def print(self):
        print("Start/End: {}/{}\nPoints:".format(self.start, self.end))
        for i in range(len(self.points)):
            print(self.points[i])

def printBoard(b):
    for i in range(1000):
        line = ""
        for j in range(1000):
            line += str(b[i][j])
        print(line)


f = open("input.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

board = [[0 for x in range(1000)] for y in range(1000)]

vents = []
for d in data:
    v = Vent(d)
    if len(v.points) > 1:
        vents.append(v)

for v in vents:
    for p in v.points:
        x = p[0]
        y = p[1]
        board[y][x] += 1

count = 0
for i in range(1000):
    for j in range(1000):
        if board[i][j] > 1:
            count += 1
print(count)