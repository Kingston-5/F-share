from os import listdir
from os.path import isfile, isdir, join
from html import ulify

public = './public'
#print(listdir('./public'))

def getFiles(directory = public):
    return [f for f in listdir(directory) if isfile(join(directory, f))]

def getDirs():
    dirs = []
    for d in listdir(public):
        if isdir(join(public, d)):
            dirs.append({d:getFiles(join(public, d))})
    return dirs

#print(f"Files: {files} \n\n")
#print(f"Dirs: {dirs} ")
