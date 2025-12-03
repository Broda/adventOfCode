import sys
import os

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

class Deer:
    def __init__(self, input) -> None:
        #Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
        a = input.split(' ')
        self.name = a[0]
        self.fly_dist = int(a[3])
        self.fly_time = int(a[6])
        self.rest_time = int(a[13])
        self.travelled = 0
        self.fly_count = 0
        self.rest_count = 0
        self.score = 0
        self.flying = True

    def __str__(self) -> str:
        return '{} travelled {} with a score of {}'.format(self.name, self.travelled, self.score)

    def tick(self):
        if self.flying:
            self.fly_count += 1
            if self.fly_count > self.fly_time:
                self.flying = False
                self.fly_count = 0
                self.rest_count = 1
                return
            else:
                self.travelled += self.fly_dist
        else:
            self.rest_count += 1
            if self.rest_count > self.rest_time:
                self.flying = True
                self.fly_count = 1
                self.rest_count = 0
                self.travelled += self.fly_dist
                return

    def getDistanceTravelled(self, time):
        remaining = time
        dist = 0
        while remaining > 0:
            if remaining < self.fly_time:
                dist += self.fly_dist * remaining
                remaining = 0
                break
            dist += self.fly_dist * self.fly_time
            remaining -= self.fly_time
            remaining -= self.rest_time
        return dist
            
def printDeer(deer):
    for d in deer.keys():
        print('{}'.format(deer[d]))

def Race(deer, time):
    dist = 0
    for d in deer.keys():
        deer[d].travelled = deer[d].getDistanceTravelled(time)
        dist = max(deer[d].travelled, dist)
    return dist
    
def Race2(deer, time):
    max_score = 0
    for _ in range(time):
        lead = ''
        lead_dist = 0
        for d in deer.keys():
            deer[d].tick()
            if deer[d].travelled > lead_dist:
                lead = d
                lead_dist = deer[d].travelled
        deer[lead].score += 1
        max_score = max(deer[lead].score, max_score)
    
    return max_score
    
def getAnswer(input):
    if '\r' in input or '\n' in input:
        input = input.replace("\r", "").split("\n")

    answer = [0,0] #part1, part2
    
    deer = {}
    for l in input:
        d = Deer(l)
        deer[d.name] = d
    
    answer[0] = Race(deer, 2503)
    printDeer(deer)

    for d in deer.keys():
        deer[d].travelled = 0

    answer[1] = Race2(deer, 2503)
    printDeer(deer)

    return answer

while(True):
    ans = getAnswer(menu())
    print(ans)
