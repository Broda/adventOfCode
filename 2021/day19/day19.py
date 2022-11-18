class Scanner:
    def __init__(self, data) -> None:
        self.data = data
        self.id = data[0].split(' ')[2] #--- scanner id ---
        self.beacons = []
        for b in range(1,len(data)):
            self.beacons.append(data[b].split(','))
        self.pos = [0,0,0]
        
    def __repr__(self) -> str:
        return f'{self.id}: {len(self.beacons)} beacons seen'


f = open("sample.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

scanners = []
s = []
for l in range(0,len(data)):
    if len(data[l]) == 0:
        scanners.append(Scanner(s))
        s = []
    else:
        s.append(data[l])

scanners.append(Scanner(s))

