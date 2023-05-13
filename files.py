from os import listdir
from os.path import isfile, isdir, join

public = './public'
print(listdir('./public'))

def getFiles():
    return [f for f in listdir(public) if isfile(join(public, f))]

def getDirs():
    return [d for d in listdir(public) if isdir(join(public, d))]

#print(f"Files: {files} \n\n")
#print(f"Dirs: {dirs} ")
