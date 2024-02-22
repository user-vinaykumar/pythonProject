# checks whether the folder exists or not. os.path.isdir() --> takes path
# of the folder to be checked.

import os

def checkfolder(folder):
    value = os.path.isdir(folder)
    if value:
        print(f'the folder {folder} exists...!!!!')
    else:
        print(f'the folder {folder} does not exists...!!!')

checkfolder('C://Users/ADMIN/PycharmProjects/pythonProject/Dictionary')
checkfolder('C://Users/ADMIN/PycharmProjects/pythonProject/folder')