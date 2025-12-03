import math

def add(num1, num2):
    return [num1,num2]

def split(num):
    num1 = math.floor(num / 2)
    num2 = math.ceil(num / 2)
    return [num1, num2]

def explode(num):
    return
    
def reduce(num):
    return

f = open("sample.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

