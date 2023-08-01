from zipfile import ZipFile
from time import sleep
import os, sys

userprofile = os.environ

path = f'{userprofile["userprofile"]}\\Downloads\\'
desktop = f'{userprofile["userprofile"]}\\Desktop'

def unZip(path, desktop):
    while True:
        sleep(0.8)
        for file in os.listdir(path):
            name_file = file
            if '.rar' and '.zip' in file:
                with ZipFile(f'{path}{file}', 'r') as zips:
                    zips.extractall(f'{desktop}\\{name_file[:-4]}')
                os.remove(f'{path}\\{file}')
if __name__ == '__main__':
    if not sys.platform == 'linux':
        unZip(path, desktop)