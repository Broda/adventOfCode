import re

class Passport:
    def __init__(self, data):
        self.data = data.replace('\n',' ').replace('\r', '').split(' ')
        self.fields = {}
        for i in self.data:
            if ':' in i:
                self.fields[i.split(':')[0]] = i.split(':')[1]

    def checkKeysExist(self):
        keys = self.fields.keys()
        if 'byr' not in keys or 'iyr' not in keys or 'eyr' not in keys or 'hgt' not in keys or 'hcl' not in keys or 'ecl' not in keys or 'pid' not in keys:
            return False
        return True

    def validYear(self, value, min, max):
        return value >= min and value <= max

    def validHeight(self, value):
        if 'cm' in value:
            hgt = int(value.replace('cm',''))
            return hgt >= 150 and hgt <= 193
        elif 'in' in value:
            hgt = int(value.replace('in',''))
            return hgt >= 59 and hgt <= 76
        return False

    def validHairColor(self, value):
        return len(re.findall("\#[0-9a-fA-F]{6}", value)) == 1

    def validEyeColor(self, value):
        eyeColors = ['amb','blu','brn','gry','grn','hzl','oth']
        return value in eyeColors

    def validPID(self, value):
        if len(value) != 9:
            return False
        return len(re.findall("[0-9]{9}", value)) == 1

    def isValid(self, checkKeysOnly = False):
        if not self.checkKeysExist():
            print("missing keys")
            return False
        
        if checkKeysOnly:
            return True

        if not self.validYear(int(self.fields['byr']), 1920, 2002):
            print("invalid byr ({})".format(self.fields['byr']))
            return False

        if not self.validYear(int(self.fields['iyr']), 2010, 2020):
            print("invalid iyr ({})".format(self.fields['iyr']))
            return False
        
        if not self.validYear(int(self.fields['eyr']), 2020, 2030):
            print("invalid eyr ({})".format(self.fields['eyr']))
            return False
        
        if not self.validHeight(self.fields['hgt']):
            print("invalid hgt ({})".format(self.fields['hgt']))
            return False

        if not self.validHairColor(self.fields['hcl']):
            print("invalid hcl ({})".format(self.fields['hcl']))
            return False
        
        if not self.validEyeColor(self.fields['ecl']):
            print("invalid ecl ({})".format(self.fields['ecl']))
            return False

        if not self.validPID(self.fields['pid']):
            print("invalid pid ({})".format(self.fields['pid']))
            return False
        
        print("valid")
        return True
        

f = open("input.txt", "r")
fdata = f.read().replace('\r','').split('\n\n')
passports = []
count = 0
for pData in fdata:
    p = Passport(pData)
    passports.append(p)
    #print(p.valid)        
    if p.isValid(False):
        count += 1

print(count)
