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
    if not os.getcwd().endswith('2024'): os.chdir('2024')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2024'): os.chdir('2024')
    f = open(path, 'w')
    f.write(s)
    f.close()

def blink(stone : int) -> list:
    if stone == 0:
        return [1]
    stone_str = str(stone)
    digits = len(stone_str)
    if digits % 2 == 0:
        half_digits = int(digits/2)
        stone1 = int(stone_str[:half_digits])
        stone2 = int(stone_str[half_digits:])
        return [stone1, stone2]
    return [stone * 2024]


def getPart1(stones : list, num_blinks : int) -> int:
    for i in range(num_blinks):
        new_stones = []
        for stone in stones:
            new_stones += blink(stone)
        stones = new_stones
    return len(stones)

def depthFirstSearch(data : dict, stone : int, blink_num : int) -> int:
    if blink_num == 0:
        return 1
    
    if (stone, blink_num) in data.keys():
        return data[(stone, blink_num)]

    count = 0
    new_stones = blink(stone)
    for s in new_stones:
        count += depthFirstSearch(data, s, blink_num-1)
    
    data[(stone, blink_num)] = count
    return count
    
    
def getPart2(stones : list, num_blinks : int) -> int:
    blink_data = {}
    count = 0
    for stone in stones:
        count += depthFirstSearch(blink_data, stone, num_blinks)
        
    #print(blink_data)
    return count

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    answer[0] = getPart1([int(x) for x in input[0].split(" ")], 25)
    answer[1] = getPart2([int(x) for x in input[0].split(" ")], 75)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
