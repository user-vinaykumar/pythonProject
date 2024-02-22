# changing the current directory of the file.
import os


def changeDirectory(item):
    os.chdir(item)  # os.chdir() is used to change the directory -- value inside () is
    # the path where file will be changed to.
    # the path we need to change is given inside ().
    print(os.getcwd())


changeDirectory('C://')
