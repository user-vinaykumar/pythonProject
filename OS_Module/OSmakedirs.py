# to create a multiple files or folders in a current directory.
import os
def makeDirectories(item):
    os.makedirs(item)
    print(f'{item} files created.')

makeDirectories('this/that/vinay/sharan') # this folder will be created and inside
# this - that folder will be created.


