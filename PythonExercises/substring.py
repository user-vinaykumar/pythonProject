# check whether the sub string present in a string.

st = 'welcome to python programming language'

sub = input('Enter the string : ')

if sub in st:
    print(f"Yes, the sub string '{sub}' present in the string.")
else:
    print(f"No, the substring '{sub}' is not present in the string.")