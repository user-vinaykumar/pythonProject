# joins path of two folders or file. (joins as a string just for an output
# and not replaces the path of files. this is only to join paths and compute.
import os
def joinPath(file1, file2):
    value = os.path.join(file1, file2)
    print(f'the path of files {file1} and {file2} are joined as {value}')

joinPath('C://', 'this.py')