class Password:
    def __init__(self, line):
        self.line = line
        l = line.split(" ")
        self.min = int(l[0].split("-")[0])
        self.max = int(l[0].split("-")[1])
        self.letter = l[1][0]
        self.pwd = l[2]
    
    def check(self):
        count = 0
        for l in self.pwd:
            if l == self.letter:
                count += 1
        return count >= self.min and count <= self.max

    def check2(self):
        p1 = self.min-1
        p2 = self.max-1

        if self.pwd[p1] == self.letter and self.pwd[p2] == self.letter:
            return False

        return self.pwd[p1] == self.letter or self.pwd[p2] == self.letter
            


f = open("input.txt", "r")
passwords = f.readlines()
good_count = 0
good_count2 = 0

plist = []
for p in passwords:
    plist.append(Password(p))

for p in plist:
    if p.check():
        good_count += 1
    if p.check2():
        good_count2 += 1

print(str(good_count))
print(str(good_count2))

