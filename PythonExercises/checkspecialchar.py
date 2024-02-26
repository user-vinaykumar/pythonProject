# check the special charecters found in a string.

import re

str = '"vinay kumar g s and sharan g s %$#@ rajeshwari and ()&"?><.,;{}[]| shivalingaiah'

regex = re.compile('%$#@()&?><.,[{]}?/.>,<|')

if regex.search(str) == None:
    print('the string does not contain special charecters...!')
else:
    print('the string does contain special charecters...!')