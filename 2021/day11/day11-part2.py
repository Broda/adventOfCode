f = open("input.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

octos = [list(d) for d in data]
for row in range(len(octos)):
    for col in range(len(octos[0])):
        octos[row][col] = int(octos[row][col])

num_octos = len(octos) * len(octos[0])

def reset_flashed_octos(flashed):
    for row in range(len(octos)):
        for col in range(len(octos[0])):
            if flashed[row][col]:
                octos[row][col] = 0

def inc_all_octos():
    for row in range(len(octos)):
        for col in range(len(octos[0])):
            octos[row][col]+=1

def try_inc_octo(row, col, flashed):
    if row < 0 or row > len(octos)-1 or col < 0 or col > len(octos[0])-1:
        return
    octos[row][col]+=1
    try_flash_octo(row, col, flashed)

def inc_neighbors(row, col, flashed):
    try_inc_octo(row-1,col,flashed) # up
    try_inc_octo(row-1,col+1,flashed) #up right
    try_inc_octo(row,col+1,flashed) #right
    try_inc_octo(row+1,col+1,flashed) #down right
    try_inc_octo(row+1,col,flashed) #down
    try_inc_octo(row+1,col-1,flashed) #down left
    try_inc_octo(row,col-1,flashed) #left
    try_inc_octo(row-1,col-1,flashed) #up left
    
def try_flash_octo(row, col, flashed):
    if row < 0 or row > len(octos)-1 or col < 0 or col > len(octos[0])-1:
        return
    if flashed[row][col] or octos[row][col]<=9:
        return
    flashed[row][col] = True
    inc_neighbors(row,col,flashed)
    
def try_flash_octos(flashed):
    for row in range(len(octos)):
        for col in range(len(octos[0])):
            try_flash_octo(row, col, flashed)
    
def count_flashed(flashed):
    count = 0
    for row in range(len(octos)):
        for col in range(len(octos[0])):
            if flashed[row][col]:
                count += 1
    return count

def check_all_zero():
    for row in range(len(octos)):
        for col in range(len(octos[0])):
            if octos[row][col] != 0:
                return False
    return True

def print_octos():
    for row in range(len(octos)):
        line = ""
        for col in range(len(octos[0])):
            line += str(octos[row][col])
        print(line)

sum = 0
step = 1
while True:
    flashed = [[False for i in range(len(octos[0]))] for j in range(len(octos))]
    inc_all_octos()
    try_flash_octos(flashed)
    reset_flashed_octos(flashed)
    count = count_flashed(flashed)
    sum += count

    if count == num_octos:
        print_octos()
        break

    if check_all_zero():
        break
    step += 1

print("Flashes: {}".format(sum))
print("First time all flashed: {}".format(step))