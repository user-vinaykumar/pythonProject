# list the files present in the current folder. gives the output in the list.
import os
def listOfDir(item):
    print(os.listdir(item))

listOfDir(item=None)

# list the files present in other folders if we pass the folder path in its ()

listOfDir('C://')