from importlib.resources import path
from pathlib import Path
import os

homeFolder = (Path.cwd()).parents[1]
print("What folder in the user directory do you want to get the size of? ")
toSize = input()

while (toSize != 'exit'):
    totalSize = 0
    for filename in os.listdir(homeFolder / toSize):
        totalSize += os.path.getsize(os.path.join((homeFolder / toSize), filename)) 
    print(totalSize)
    print ('In GB: ' + str(totalSize / 1073741824))
    print(list( (homeFolder / toSize).glob('*.txt')))
    print("What folder in the user directory do you want to get the size of? ")
    toSize = input()