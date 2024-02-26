#  Write a Python program to count the number of strings from a given list of strings.
#  The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

mall = ['abc', 'xyz', 'aba', '1221']


def problem1(item):
    count = 0
    for i in item:
        k = len(i)
        if k >2:
            if i[0] == i[-1]:
                count+=1
            else:
                continue
        else:
            continue
    print(f'output : {count}')


problem1(mall)