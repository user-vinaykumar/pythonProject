# check whether the two sets are having similar items in them.

set1 = {'red', 'green', 'purple', 'blue', 'black', 'white'}
set2 = {'red', 'green', 'purple', 'blue', 'black', 'orange'}

set3 = {'mandya', 'mysuru', 'bengaluru', 'ramanagara'}
set4 = {'chamarajanagara', 'hassana', 'tumakuru', 'kolara'}

def noElementCommon(item, item1):
    for i in item:
        if i in item1:
            iscommon = False
        else:
            iscommon = True

    if iscommon:
        print(f'the two defined sets does not have a common elements.')
    else:
        print(f'the two defined sets does have a common elements.')

noElementCommon(set4, set3)