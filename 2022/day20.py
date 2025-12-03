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
    if not os.getcwd().endswith('2022'): os.chdir('2022')
    f = open(path, "r")
    return f.read().strip()

def mix(file, times=1):
    l = len(file)
    indices = [i for i in range(len(file))]

    for t in range(times):
        for i, v in enumerate(file):
            if v == 0: continue
            j = indices.index(i)
            num = indices.pop(j)
            next_index = (j+v) % (l - 1)
            indices.insert(next_index, num)

    return [file[i] for i in indices]

def getCoords(file):
    l = len(file)
    return sum(file[i] for i in (
        (file.index(0) + m) % l for m in [1000,2000,3000]))
    
def getAnswer(input, isSample):
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    decrypt_key = 811589153
    file = list(map(int, input))
    file2 = [i * decrypt_key for i in file]

    answer[0] = getCoords(mix(file, 1))
    answer[1] = getCoords(mix(file2, 10))

    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
