# check whether the path exists or not. os.path.exists() --> takes path of the
# folder/file to check.
import os.path


def pathcheck(item):
    value = os.path.exists(item)
    if value:
        print(f'the path entered -- {item} is exists!!!')
    else:
        print(f'the path entered -- {item} does not exists!!!')


pathcheck('C://')
pathcheck('C://vinay.txt')
pathcheck('C://Program Files')
