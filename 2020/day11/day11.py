import copy

def print_board(b):
    for row in range(ROWS):
        line = ""
        for col in range(COLS):
            line += b[row][col]
        print(line)

def valid_seat(row, col):
    if row < 0 or row > ROWS-1 or col < 0 or col > COLS-1:
        return False
    return True

def add_seat_if_valid(row, col, seats):
    if valid_seat(row,col):
        seats.append([row,col])

def get_adj_seats(row, col):
    seats = []
    add_seat_if_valid(row-1,col-1,seats)
    add_seat_if_valid(row-1,col,seats)
    add_seat_if_valid(row-1,col+1,seats)
    add_seat_if_valid(row,col-1,seats)
    add_seat_if_valid(row,col+1,seats)
    add_seat_if_valid(row+1,col-1,seats)
    add_seat_if_valid(row+1,col,seats)
    add_seat_if_valid(row+1,col+1,seats)
    return seats
    
def adj_occupied_count(b, row, col):
    count = 0
    adj = get_adj_seats(row, col)
    for s in adj:
        if b[s[0]][s[1]] == '#':
            count += 1
    return count
    
def find_seat(curr_b, changes):
    for row in range(ROWS):
        for col in range(COLS):
            if curr_b[row][col] == 'L' and adj_occupied_count(curr_b, row, col) == 0:
                changes.append([row,col])

def leave_seat(curr_b, changes):
    for row in range(ROWS):
        for col in range(COLS):
            cnt = adj_occupied_count(curr_b, row, col)
            if curr_b[row][col] == '#' and cnt >= 4:
                changes.append([row,col])

def update_board(curr_b, changes):
    for c in changes:
        curr_b[c[0]][c[1]] = flips[curr_b[c[0]][c[1]]]

def count_occupied(curr_b):
    count = 0
    for row in range(ROWS):
        for col in range(COLS):
            if curr_b[row][col] == "#":
                count += 1
    return count

def part1(b):
    count = 1
    
    while True:
        changes = []

        find_seat(b, changes)
        leave_seat(b, changes)

        chg_count = len(changes)
        #print("{} changes".format(chg_count))
        if chg_count == 0:
            print("{} occupied".format(count_occupied(b)))
            break
        
        update_board(b, changes)
        changes = []

        count += 1
        if count > 1000:
            print("fail")
            break

def part2(b):
    count = 1
    
    while True:
        changes = []

        find_seat(b, changes)
        leave_seat(b, changes)

        chg_count = len(changes)
        #print("{} changes".format(chg_count))
        if chg_count == 0:
            print("{} occupied".format(count_occupied(b)))
            break
        
        update_board(b, changes)
        changes = []

        count += 1
        if count > 1000:
            print("fail")
            break


f = open("input.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

board = [list(x) for x in data]

ROWS = len(board)
COLS = len(board[0])

flips = {'L':'#', '#':'L', '.':'.'}

part1(board)
