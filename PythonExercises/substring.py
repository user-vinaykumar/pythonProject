# check whether the sub string present in a string.

st = 'welcome to python programming language'

sub = input('Enter the string : ')

if sub in st:
    print(f"Yes, the sub string '{sub}' present in the string.")
else:
    print(f"No, the substring '{sub}' is not present in the string.")



# second approach by using find() function.


subs = input('Enter the word : ')

indx = st.find(subs)

if indx>=0:
    bool = True
else:
    bool = False

if bool:
    print(f"Yes, the substring '{subs}' present in the string.")
else:
    print(f"No, the substring '{subs}' not present in the string.")

