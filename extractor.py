import os
import zipfile

master_directory = ""

def start(masterdir):
    with os.scandir(masterdir) as entries:
        for entry in entries:
            if entry.is_dir():
                print(entry.path)
                findZips(entry.path)

def findZips(dir):
    with os.scandir(dir) as files:
        for file in files:
            if file.name.endswith('.zip'):
                    extractZip(file)

def extractZip(file):
    newFileName = file.name.split('.')
    zip = zipfile.ZipFile(file, 'r')
    zip.extractall(path=f'{os.path.dirname(file.path)}\\{newFileName[0]}\\')
    zip.close()

start(master_directory)
print("Done.")