# renames the file with os.rename('currentfile_name', 'new_filename')
import os
def renamethefile(old, new):
    os.rename(old, new)
    print(f'{old} name is replaced by new name {new}')

renamethefile('this.py', 'sharan.py')