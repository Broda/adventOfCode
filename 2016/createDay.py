import os
import shutil

def copyFile(num):
    if not os.getcwd().endswith('2016'): os.chdir('2016')
    src = './day.py'
    dest = f'./day{num}.py'
    shutil.copy(src, dest)
    writeFile(f'./day{num}sample.txt', '')

def writeFile(path, s):
    if not os.getcwd().endswith('2016'): os.chdir('2016')
    f = open(path, 'w')
    f.write(s)
    f.close()

num = int(input("Day #: "))
if num < 10:
    copyFile("0" + str(num))
else:
    copyFile(str(num))
