# check the element whether it is present or not in a tuple.

sample = ('w', 3, 'r', 'e', 's', 'o', 'u', 'r', 'c', 'e')


def solution(item, checkNum):
    if checkNum in item:
        print(f'the element {checkNum} present in the tuple {item}')
    else:
        print(f'the element {checkNum} does not present in the tuple {item}')

solution(sample, 'r')
print('----------------------------------------------')
solution(sample, 'j')