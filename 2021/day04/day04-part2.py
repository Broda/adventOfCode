class Board:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.rows = data.split("\n")
        self.cols = [[0 for x in range(5)] for y in range(5)]
        for i in range(5):
            self.rows[i] = self.rows[i].strip().split(' ')
            while("" in self.rows[i]):
                self.rows[i].remove("")

        for j in range(5):
            for i in range(5):
                self.cols[j][i] = self.rows[i][j]

    def __str__(self):
        return self.data

    def checkForWin(self, marked):
        for i in range(5):
            tempRow = self.rows[i].copy()
            tempCol = self.cols[i].copy()
            for j in range(len(marked)):
                if marked[j] in tempRow:
                    tempRow.remove(marked[j])
                if marked[j] in tempCol:
                    tempCol.remove(marked[j])
            if len(tempRow) == 0 or len(tempCol) == 0:
                return True

        return False
    
    def score(self, marked):
        score = 0
        if len(marked) == 0:
            return score

        for i in range(5):
            for j in range(5):
                if self.rows[i][j] not in marked:
                    score += int(self.rows[i][j])
        
        l = len(marked)-1
        print("sum = {}".format(score))
        score *= int(marked[l])
        return score

f = open("input.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

numbers = data[0].split(',')
marked = []

boards = []
board = ""
id = 1
for i in range(2, len(data)):
    if len(data[i]) > 0:
        if len(board) > 0:
            board += "\n"
        board += data[i]
    else:
        boards.append(Board(id, board))
        board = ""
        id += 1
boards.append(Board(id, board))
        
winner = None
for m in numbers:
    if winner is None and len(boards) == 1:
        winner = boards[0]
        
    marked.append(m)
    newlist = []
    for b in boards:
        if not b.checkForWin(marked):
            newlist.append(b)
        else:
            print("removing board # {}".format(b.id))

    boards = newlist
    if len(boards) == 0:
        break

if winner is not None:
    print("board # {} WINS".format(winner.id))
    print(winner.score(marked))
else:
    print("no winner")