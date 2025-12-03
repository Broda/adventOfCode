costs = {'A':1,'B':10,'C':100,'D':1000}

class Pod:
    def __init__(self, name, energy_cost, loc):
        self.name = name
        self.cost = energy_cost
        self.location = loc
        self.energy_used = 0

    def __str__(self) -> str:
        return self.name + ' @ ' + str(self.location) + ', cost=' + str(self.cost) + ', used=' + str(self.energy_used)

    def move(self, dest):
        moves = abs(self.location[0] - dest[0]) + abs(self.location[1] - dest[1])
        self.energy_used = moves * self.cost
        self.location = dest


class RoomMap:
    def __init__(self, data):
        self.data = data
        self.map = []
        self.pods = []
        self.loadData()

    def __str__(self) -> str:
        s = ''
        for r in range(len(self.map)):
            s += self.map[r] + '\n'
        return s

    def loadData(self):
        # data[0] = top wall
        # data[1][1] - data[1][11] = hall
        # data[2, 3][3, 5, 7, 9] = homes
        for r in range(len(self.data)):
            self.map.append(self.data[r])
        
        for r in [2,3]:
            for c in [3,5,7,9]:
                self.pods.append(Pod(self.map[r][c], costs[self.map[r][c]], [r,c]))
    
    def roomIsPassable(self, r, c):
        return self.map[r][c] == '.'
                    
    def roomIsHall(self, r, c):
        return r > 0 and r < 12 and c == 1
    
    def roomIsHome(self, r, c):
        return r in [2,3] and c in [3,5,7,9] 

        
f = open("sample.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")


Map = RoomMap(data)
print(Map)

for p in Map.pods:
    print(p)