f = open("sample.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

pos = [0,0,0]

for i in range(len(data)):
    move = data[i].split(' ')
    if move[0] == 'forward':
        pos[0] += int(move[1])
        pos[1] += (int(move[1]) * pos[2])
    elif move[0] == 'down':
        pos[2] += int(move[1])
    elif move[0] == 'up':
        pos[2] -= int(move[1])
    
print(pos)
print(pos[0] * pos[1])