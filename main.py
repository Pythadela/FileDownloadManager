import os

source = 'C:\\Users\\Pythadela\\Downloads'

with os.scandir(source) as entries:
        for entry in entries:
            print(entry.name)
 
