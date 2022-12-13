import sys
import os
from itertools import permutations

def readFile(path):
    if not os.getcwd().endswith('2015'): os.chdir('2015')
    f = open(path, "r")
    return f.read().strip()

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
            return readFile(samplePath)
        case "2":
            return readFile(inputPath)
        case "3":
            return readFile(input("File Name: "))
        case "4":
            return input("Input: ")
        case _:
            print("Invalid option. Try Again.\n")
            return menu()

def getBestCookieScore(ingredients, scores):
    best = 0
    all_perms = []
    
    for i in range(1,len(ingredients)+1):
        p = list(permutations(ingredients, i))
        all_perms += p

    for p in all_perms:
        score = 0
        if len(p) == 1:
            cap = 100 * scores[p[0]]['capacity']
            dur = 100 * scores[p[0]]['durability']
            fla = 100 * scores[p[0]]['flavor']
            tex = 100 * scores[p[0]]['texture']
            print(cap, dur, fla, tex)
            cap = cap if cap >= 0 else 0
            dur = dur if dur >= 0 else 0
            fla = fla if fla >= 0 else 0
            tex = tex if tex >= 0 else 0
            print(cap, dur, fla, tex)
            score = cap * dur * fla * tex
            best = max(best, score)
        else:
            pass
        
    return best

def getAnswer(input):
    if '\r' in input or '\n' in input:
        input = input.replace("\r", "").split("\n")

    answer = [0,0] #part1, part2
    
    ingredients = set()
    scores = dict()
    for l in input:
        # Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
        name, values = l.split(':')
        ingredients.add(name)
        values = values.strip().split(', ')
        for v in values:
            value = v.split(' ')
            scores.setdefault(name, dict())[value[0]] = int(value[1])
        
    answer[0] = getBestCookieScore(ingredients, scores)
    

    return answer

while(True):
    ans = getAnswer(menu())
    print(ans)
