
f = open("sample.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")[0]

positions = data.split(',')
positions = sorted([int(x) for x in positions])

numpos = len(positions)
minpos = positions[0]
maxpos = positions[numpos-1]

print("# positions: {}, min: {}, max: {}".format(numpos, minpos, maxpos))

def getFuelCost(crabs, pos):
    cost = 0
    for c in crabs:
        cost += abs(c - pos)
    return cost

bestpos = -1
mincost = 99999999999
for i in range(minpos, maxpos+1):
    cost = getFuelCost(positions, i)
    if cost < mincost:
        mincost = cost
        bestpos = i

print("Position #{} = {}".format(bestpos, mincost))
