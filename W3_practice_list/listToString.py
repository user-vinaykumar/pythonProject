# print the list of charecters into a single string.

list = ['v', 'i', 'n', 'a', 'y']

def list_to_string(item):
    result = ''
    for i in item:
        result+=i
    print(result)

list_to_string(list)