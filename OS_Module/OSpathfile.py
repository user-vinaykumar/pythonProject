# checks whether the file present or not

import os


def checkfile(file):
    value = os.path.isfile(file)
    if value:
        print(f'the file {file} exists!!!')
    else:
        print(f'the file {file} does not exists!!!')


checkfile('C://Users/ADMIN/Documents/vinay.txt')
checkfile('C://Users/ADMIN/Documents/sharan.txt')
