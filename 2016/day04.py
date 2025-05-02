import os
import sys

def menu():
    main = "\nPlease choose an input option:\n"
    main += "1. Sample File\n"
    main += "2. Input File\n"
    main += "3. Other File\n"
    main += "4. Prompt\n"
    main += "5. Quit\n"
    main += ">> "
    
    filename = os.path.basename(__file__)
    samplePath = filename.replace('.py', 'sample.txt')
    inputPath = filename.replace('.py', 'input.txt')
    
    match input(main):
        case "5":
            sys.exit(0)
        case "1":
            isSample = True
            return readFile(samplePath), True
        case "2":
            return readFile(inputPath), False
        case "3":
            return readFile(input("File Name: ")), False
        case "4":
            return input("Input: "), False
        case _:
            print("Invalid option. Try Again.\n")
            return menu()

def readFile(path):
    if not os.getcwd().endswith('2016'): os.chdir('2016')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2016'): os.chdir('2016')
    f = open(path, 'w')
    f.write(s)
    f.close()

# if room is real, returns sector ID, else returns 0
def isRealRoom(data : str) -> int:
    room = "".join(list(data.split("[")[0].split("-")[:-1]))
    id = int(data.split("[")[0].split("-")[-1])
    csum = data.split("[")[1][:-1]
    #print(f'room: {room}, ID: {id}, csum: {csum}')

    chars = {}
    for c in room:
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    
    numbers = {}
    for k in chars.keys():
        if chars[k] not in numbers:
            numbers[chars[k]] = [k]
        else:
            numbers[chars[k]].append(k)
            numbers[chars[k]].sort()
    
    counts = list(numbers.keys())
    counts.sort(reverse=True)
    
    shouldbe = ""
    curr = counts.pop(0)
    for x in range(5):
        shouldbe += numbers[curr].pop(0)
        if len(numbers[curr]) == 0 and len(counts) > 0: curr = counts.pop(0)
    
    if shouldbe == csum: return id

    return 0

def shiftLetter(letter : str, times : int) -> str:
    times = times % 26
    code = ord(letter)
    code += times
    if code > ord("z"): 
        code -= 26
    return chr(code)

def getPart1(input) -> int:
    sectorIDSum = 0

    for room in input:
        sectorIDSum += isRealRoom(room)

    return sectorIDSum

def getPart2(input) -> int:
    rooms = []
    for room in input:
        id = isRealRoom(room)
        if id > 0:
            room = room.split("-" + str(id))[0]
            decrypted = ""
            for c in room:
                if c == "-":
                    decrypted += " "
                else:
                    decrypted += shiftLetter(c, id)
            rooms.append([id, decrypted])

    for room in rooms:
        if "pole" in room[1]:
            print(room)
            return room[0]

    return 0

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2


    answer[0] = getPart1(input)
    answer[1] = getPart2(input)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
