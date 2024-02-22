# creates file / folder in the current folder.

import os


def createdir(item):
    os.mkdir(item)
    print(f'{item} file created.')


createdir('this.py')  # creates 'this' file / folder in OS_Module folder.

# only one file or folder can be created. for multiple file or folder we have another method.
