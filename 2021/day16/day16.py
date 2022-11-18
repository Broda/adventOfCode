class Packet:
    def __init__(self, data):
        self.rawData = data
        self.version = int(data[0:3],2)
        self.typeId = int(data[3:6],2)
        self.remainingData = data[6:]
        self.subpackets = []

        if self.typeId == 4:
            self.literalVal = self.decodeLiteral()
        else:
            self.literalVal = -1
            self.decodeOperator()

    def decodeLiteral(self):
        lit = ''
        index = 0
        number = self.remainingData[index:index+5]
        while True:
            
            lit += number[1:5]
            if number[0] == '1':
                index = index+5
                number = self.remainingData[index:index+5]
            else:
                break
        return int(lit,2)

    def decodeOperator(self):
        lenType = self.remainingData[0]
        length = self.remainingData[1:12]
        substart = 12
        if lenType == '0':
            length += self.remainingData[12:16]
            substart = 16
        print(int(length,2))
        self.subpackets = []
        sub = ''
        
        return

    def __str__(self):
        return '{}: {} / {}'.format((self.version, self.typeId), self.literalVal, self.subpackets)

f = open("input.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")[0].upper()

#print(data)
hex_to_bits = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111'
}

#sample1
#data = 'D2FE28'
#sample2
data = '38006F45291200'

binary = ''
for c in data:
    binary += hex_to_bits[c]


p = Packet(binary)
print(p)