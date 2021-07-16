import os
from tkinter import filedialog
from tkinter import *
root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()


def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles
allfile=getListOfFiles(folder_selected)
count=0
for i in allfile:
	count+=1
	file_size = os.path.getsize(i)
	if file_size<1048576 and file_size>2048:
		print('File path',i,"File Size is :", file_size, "bytes")

print(count)
while TRUE:
	continue