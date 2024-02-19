# print the max value of the names list a.k.a the name with more charecters.

names = ['vinay', 'sharan', 'rajeshwari']

print(max(names, key=len))  # for key= we should always give a function as
                                # value, here len is given without ().

