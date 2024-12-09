import os
import shutil

def copyFile(num):
    if not os.getcwd().endswith('2024'): os.chdir('2024')
    src = './day.py'
    dest = f'./day{num}.py'
    shutil.copy(src, dest)
    writeFile(f'./day{num}sample.txt', '')

def writeFile(path, s):
    if not os.getcwd().endswith('2024'): os.chdir('2024')
    f = open(path, 'w')
    f.write(s)
    f.close()

num = input("Day #: ")
copyFile(num)
