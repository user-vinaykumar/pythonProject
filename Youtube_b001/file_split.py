# split the file names by their extension

import os

full_files = ['info.txt',
              'image.png',
              'script.c',
              'image2.jpg',
              'info.3.txt']


# print without their extension

def splitFilesByExtension(item):
    fileList = []
    for i in item:
        fileName = os.path.splitext(i)
        fileList.append(fileName[0])
    for k in fileList:
        print(k)


(splitFilesByExtension(full_files))

print('-------------------------')


# second way of doing this

def splitFile(item):
    for i in item:
        FullFileName = os.path.splitext(i)[0]
        print(FullFileName)


splitFile(full_files)
