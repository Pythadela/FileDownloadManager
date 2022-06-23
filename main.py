import os

source_dir = 'C:\\Users\\Pythadela\\Downloads'

with os.scandir(source_dir) as entries:
        for entry in entries:
            print(entry.name)
