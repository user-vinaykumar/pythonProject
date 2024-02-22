import os  # standard import from standard library of python.
from Python_module import indexfinder  # custom import imported from the module created earlier.

print(dir(os))  # gives the list of methods present in the OS module.

indx = indexfinder(dir(os), 'getcwd')  # imported the Python module that helps in
# finding the index of 'getcwd' method present in the dir(os)

print(indx)
print(len(dir(os)))
