#seat = list("BBFFBBFRLL")

def getSeatID(seat):
    seat = list(seat)
    currRange = range(128)

    while len(currRange) > 1:
        half = int(len(currRange)/2)
        if seat.pop(0) == "F":
            currRange = currRange[:half]
        else:
            currRange = currRange[half:]

    row = currRange[0]

    currRange = range(8)
    while len(currRange) > 1:
        half = int(len(currRange)/2)
        #print(half)
        if seat.pop(0) == "R":
            currRange = currRange[half:]
            #print("R [{}]".format(currRange))
        else:
            currRange = currRange[:half]
            #print("L [{}]".format(currRange))
        
    col = currRange[0]
    #print("row {} col {}".format(row, col))
    seatID = row * 8 + col
    #print("seat ID: {}".format(seatID))
    return seatID

f = open("input.txt", "r")
seatlines = f.read().splitlines()
highID = -1

seats = []
for s in seatlines:
    seatID = getSeatID(s)
    seats.append(seatID)

seats.sort()
start = seats[0]
seatID = -1
print(seats[len(seats)-1])

for i in range(1, len(seats)):
    curr = seats[i]
    if curr == start+1:
        start = curr
        continue
    if curr == start+2:
        seatID = start+1
        break

    
print(seatID)