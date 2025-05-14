import os
import shutil

def copyFile(num):
    if not os.getcwd().endswith('2017'): os.chdir('2017')
    src = './day.py'
    dest = f'./day{num}.py'
    shutil.copy(src, dest)
    writeFile(f'./day{num}sample.txt', '')

def writeFile(path, s):
    if not os.getcwd().endswith('2017'): os.chdir('2017')
    f = open(path, 'w')
    f.write(s)
    f.close()

def padNum(num : int) -> str:
    temp = str(num)
    if len(temp) < 2:
        temp = f"0{temp}"
    return temp

num = int(input("Day Start #: "))
num2 = int(input("Day End #: "))
for i in range(num, num2+1):
    copyFile(padNum(i))
