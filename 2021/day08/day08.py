
# 0 = 6 seg
# 1 = 2 seg *
# 2 = 5 seg
# 3 = 5 seg
# 4 = 4 seg *
# 5 = 5 seg
# 6 = 6 seg
# 7 = 3 seg *
# 8 = 7 seg *
# 9 = 6 seg

class DisplayNumber:
    def __init__(self, _data):
        self.data = _data
        self.num = -1
        self.nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.segs = {}
        for i in range(7):
            self.segs[i] = "abcdefg"
        self.load()
    
    def print(self):
        print("Data: {}\nNum: {}\nNums: {}\nSegs: {}\n-----".format(self.data, self.num, self.nums, self.segs))

    def load(self):
        _len = len(self.data)
        if _len == 2:
            self.num = 1
            self.nums = [1]
            for i in range(7):
                if i not in [3,6]:
                    self.segs[i] = ""
                else:
                    self.segs[i] = self.data
        elif _len == 3:
            self.num = 7
            self.nums = [7]
            for i in range(7):
                if i not in [0,3,6]:
                    self.segs[i] = ""
                else:
                    self.segs[i] = self.data
        elif _len == 4:
            self.num = 4
            self.nums = [4]
            for i in range(7):
                if i not in [1, 2, 3, 6]:
                    self.segs[i] = ""
                else:
                    self.segs[i] = self.data
        elif _len == 5:
            self.num = -1
            self.nums = [2, 3, 5]
        elif _len == 6:
            self.num = -1
            self.nums = [0, 6, 9]
            
        elif _len == 7:
            self.num = 8
            self.nums = [8]

class Display:
    def __init__(self, _data):
        self.data = _data
        self.length = len(self.data)
        self.inputs = []
        self.outputs = []
        self.segs = {}
        self.unique = 0
        for i in range(0, 10):
            self.segs[i] = 0
        self.load()
    
    def load(self):
        self.inputs_raw, self.outputs_raw = self.data.split('|')
        self.inputs_raw = self.inputs_raw.strip()
        self.input_strings = self.inputs_raw.split(' ')
        self.outputs_raw = self.outputs_raw.strip()
        self.output_strings = self.outputs_raw.split(' ')
        self.inputs = []
        self.outputs = []
        self.numbers = {}
        self.segs = []

        for i in range(7):
            self.segs.append('abcdefg')

        for i in range(10):
            self.numbers[i] = None
            self.input_strings[i] = "".join(sorted(self.input_strings[i]))
            self.inputs.append(DisplayNumber(self.input_strings[i]))
        
        for i in range(len(self.output_strings)):
            self.output_strings[i] = "".join(sorted(self.output_strings[i]))
            self.outputs.append(DisplayNumber(self.output_strings[i]))
            
    def descramble(self):
        for n in self.inputs:
            if n.num != -1:
                self.numbers[n.num] = n

        self.segs[0] = self.numbers[7].data
        for c in self.numbers[1].data:
            self.segs[0] = self.segs[0].replace(c, '')
            self.segs[1] = self.segs[1].replace(c, '')
            self.segs[2] = self.segs[1].replace(c, '')
            self.segs[4] = self.segs[1].replace(c, '')
            self.segs[5] = self.segs[1].replace(c, '')
        self.segs[1] = self.segs[1].replace(self.segs[0], '')
        self.segs[2] = self.segs[2].replace(self.segs[0], '')
        self.segs[3] = self.numbers[1].data
        self.segs[4] = self.segs[4].replace(self.segs[0], '')
        self.segs[5] = self.segs[5].replace(self.segs[0], '')
        self.segs[6] = self.numbers[1].data
        
        for c in self.segs[1]:
            if c not in self.numbers[4].data:
                self.segs[1] = self.segs[1].replace(c,'')
                self.segs[2] = self.segs[1]
        
        for n in self.inputs:
            if len(n.data) == 5:
                if self.numbers[1].data[0] in n.data and self.numbers[1].data[1] in n.data:
                    n.num = 3
                    n.nums = [3]
                    self.numbers[3] = n
                    break
        for c in self.numbers[4].data:
            self.segs[4] = self.segs[4].replace(c,'')
            self.segs[5] = self.segs[5].replace(c,'')
            if c in self.numbers[3].data and c not in self.numbers[1].data:
                self.segs[2] = c
                self.segs[1] = self.segs[1].replace(c,'')
                self.segs[4] = self.segs[4].replace(c,'')
                self.segs[5] = self.segs[5].replace(c,'')
                self.segs[4] = self.segs[4].replace(self.segs[1],'')
                self.segs[5] = self.segs[5].replace(self.segs[1],'')
                break
        
        for n in self.inputs:
            if len(n.data) == 6:
                if self.segs[2] not in n.data:
                    n.num = 0
                    n.nums = [0]
                    self.numbers[0] = n
                    break
        
        for c in self.numbers[3].data:
            if c not in self.numbers[7].data and c not in self.numbers[1].data and c not in self.numbers[4].data:
                self.segs[5] = c
                self.segs[4] = self.segs[4].replace(c,'')

        for n in self.inputs:
            if len(n.data) == 6:
                if self.segs[2] in n.data and self.numbers[1].data[0] in n.data and self.numbers[1].data[1] in n.data:
                    n.num = 9
                    n.nums = [9]
                    self.numbers[9] = n
                    break
        for n in self.inputs:
            if len(n.data) == 6:
                if n.data != self.numbers[0].data and n.data != self.numbers[9].data:
                    n.num = 6
                    n.nums = [6]
                    self.numbers[6] = n
            if len(n.data) == 5 and n.data != self.numbers[3].data:
                if self.segs[4] in n.data:
                    n.num = 2
                    n.nums = [2]
                    self.numbers[2] = n
                    if self.segs[3][0] in n.data:
                        self.segs[3] = self.segs[3][0]
                        self.segs[6] = self.segs[6].replace(self.segs[3],'')
                    else:
                        self.segs[6] = self.segs[6][0]
                        self.segs[3] = self.segs[3].replace(self.segs[6],'')
        
        temp = self.input_strings.copy()
        for i in range(10):
            if self.numbers[i] is not None:
                if self.numbers[i].data in self.input_strings:
                    temp.remove(self.numbers[i].data)
        
        for n in self.inputs:
            if n.data == temp[0]:
                n.num = 5
                n.nums = [5]
                self.numbers[5] = n
        
        self.codes = {}
        for i in range(10):
            self.codes[self.numbers[i].data] = i

        self.output = ""
        for s in self.output_strings:
            self.output += str(self.codes[s])
        
        self.output = int(self.output)
        return

    def print(self):
        for i in range(10):
            if self.numbers[i] is None:
                print("{}: None".format(i))
            else:
                print("{}: {}".format(i, self.numbers[i].data))

    def print_segs(self):
        for i in range(7):
            print("{}: {}".format(i, self.segs[i]))


f = open("input.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

count = 0
for i in range(0, len(data)):
    disp = Display(data[i])
    disp.descramble()
    count += disp.output

print(count)

