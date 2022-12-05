<<<<<<< HEAD
from copy import deepcopy
=======
>>>>>>> cffc818a6d0d6edcf82c525932513a9734691a38
from collections import defaultdict

def printImg(img):
    for row in range(len(img)):
        line = ""
        for col in range(len(img[0])):
            line += img[row][col]
        print(line)

<<<<<<< HEAD
def enhance(img, inc):
    num_rows = len(img) + inc
    num_cols = len(img[0]) + inc
    new_input = [['.' for c in range(num_cols)] for r in range(num_rows)]
    half = int(inc/2)

    output = deepcopy(new_input)
    for r in range(half, num_rows-half):
        for c in range(half, num_cols-half):
            new_input[r][c] = img[r-half][c-half]
=======
def enhance(img):
    num_rows = len(img) + 2
    num_cols = len(img[0]) + 2
    new_input = [['0' for c in range(num_cols)] for r in range(num_rows)]
    
    output = new_input.copy()
    for r in range(1, num_rows-1):
        for c in range(1, num_cols-1):
            new_input[r][c] = img[r-1][c-1]
>>>>>>> cffc818a6d0d6edcf82c525932513a9734691a38
    # printImg(new_input)
    # print("")

    for r in range(num_rows):
        for c in range(num_cols):
            index = getAlgoIndex(new_input, r, c)
            output[r][c] = algo[index]

<<<<<<< HEAD
    #new_output = [[output[r][c] for c in range(1, num_cols-1)] for r in range(1, num_rows-1)]

    return output
=======
    new_output = [[output[r][c] for c in range(1, num_cols-1)] for r in range(1, num_rows-1)]

    return new_output
>>>>>>> cffc818a6d0d6edcf82c525932513a9734691a38

def getAlgoIndex(img, row, col):
    binNum = ''
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r < 0 or r > len(img)-1 or c < 0 or c > len(img[0])-1:
                binNum += '0'
            else:
                binNum += getBinaryDigit(img[r][c])
    return int(binNum,2)

def getBinaryDigit(char):
    if char == '#':
        return '1'
    else:
        return '0'

def getLitCount(img):
    count = 0
    for r in range(len(img)):
        for c in range(len(img[0])):
            if img[r][c] == '#':
                count += 1
    return count

f = open("input.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

algo = data[0]
img_input = []
for l in range(2, len(data)):
    img_input.append(list(data[l]))

printImg(img_input)
print("")
print("Lit Count: {}\n".format(getLitCount(img_input)))

<<<<<<< HEAD
img_output = enhance(img_input, 20)
=======
img_output = enhance(img_input)
>>>>>>> cffc818a6d0d6edcf82c525932513a9734691a38
printImg(img_output)
print("")
print("Lit Count: {}\n".format(getLitCount(img_output)))

<<<<<<< HEAD
img_output = enhance(img_output, 20)
=======
img_output = enhance(img_output)
>>>>>>> cffc818a6d0d6edcf82c525932513a9734691a38
printImg(img_output)
print("")
print("Lit Count: {}\n".format(getLitCount(img_output)))

<<<<<<< HEAD
output = []
for row in range(len(img_output)-8):
    if row <= 7:
        continue
    r = []
    for col in range(len(img_output[0])-8):
        if col <= 7:
            continue
        r.append(img_output[row][col])
    output.append(r)

printImg(output)
print("Lit Count: {}\n".format(getLitCount(output)))

print("rows: {}, cols: {}".format(len(img_input), len(img_input[0])))
print("rows: {}, cols: {}".format(len(img_output), len(img_output[0])))
print("rows: {}, cols: {}".format(len(output), len(output[0])))
=======
print("rows: {}, cols: {}".format(len(img_input), len(img_input[0])))
print("rows: {}, cols: {}".format(len(img_output), len(img_output[0])))
>>>>>>> cffc818a6d0d6edcf82c525932513a9734691a38
