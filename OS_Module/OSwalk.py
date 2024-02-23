# prints the entire tree of the directory until it covers every file.
import os

print(os.getcwd()) # current directory path --> to pass inside the walk()
print('------------')

# for path, folders, files in os.walk('C:/Users/ADMIN/PycharmProjects/pythonProject/OS_Module'):
#     print(f'directory path : {path}')
#     print(f'folders inside a directory : {folders}')
#     print(f'files inside folders : {files}')
#     print('----------')


for path, folders, files in os.walk('C:/Users/ADMIN/PycharmProjects/pythonProject'):
    print(f'directory path : {path}')
    print(f'folders inside a directory : {folders}')
    print(f'files inside folders : {files}')
    print('----------')