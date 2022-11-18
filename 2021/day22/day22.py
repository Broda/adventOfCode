from functools import lru_cache

f = open("input.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

reactor = [[[False for z in range(-50,51)] for y in range(-50,51)] for x in range(-50,51)]

@lru_cache(maxsize=None)
def countOn():
    count = 0
    for x in range(-50,51):
        for y in range(-50,51):
            for z in range(-50,51):
                if reactor[x][y][z]:
                    count += 1
    return count

@lru_cache(maxsize=None)
def getRange(pos):
    start, end = pos.split('=')[1].split('..')
    start = int(start)
    end = int(end)
    if start > 50 or end < -50:
        return start, start-1
    if start < -50:
        start = -50
    if end > 50:
        end = 50

    return start, end+1

@lru_cache(maxsize=None)
def runCmd(cmd):
    turnOn = cmd.split(' ')[0] == 'on'
    pos = cmd.split(' ')[1].split(',')
    
    start_x, end_x = getRange(pos[0])
    start_y, end_y = getRange(pos[1])
    start_z, end_z = getRange(pos[2])
    if end_x < start_x or end_y < start_y or end_z < start_z:
        return
    #print(f'x={start_x}..{end_x},y={start_y}..{end_y},z={start_z}..{end_z}')
    for x in range(start_x, end_x):
        if x < -50 or x > 50:
            continue
        for y in range(start_y, end_y):
            if y < -50 or y > 50:
                continue
            for z in range(start_z, end_z):
                if z < -50 or z > 50:
                    continue
                reactor[x][y][z] = turnOn

for cmd in data:
    runCmd(cmd)

print(countOn())