# get a string to be entered from an user and return N/A if user does not enter anything.

word = input('Enter the string : ')

def inp(char):
    name = word or 'N/A'
    return name

print(inp(word))

