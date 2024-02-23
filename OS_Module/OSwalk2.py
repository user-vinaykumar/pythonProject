# continuation of OSwalk
import os

for path, folders, files in os.walk('C:/Users/ADMIN/Documents'):
    print(f'path of the directory : {path}')
    print(f'folders present in this directory : {folders}')
    print(f'all files present in this directory : {files}')
    print('---------------')


print(os.stat("C:/Users/ADMIN/Documents/Sound recordings/Recording.m4a").st_size)