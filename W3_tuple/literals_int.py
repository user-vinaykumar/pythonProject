# convert the positive integers to single integer number.
# input = (1, 2, 3) ==> 123 as output.

sample = (1,2,3,4)

def solution(item):
    x = ''
    for i in item:
        x+=str(i)
    print(f'the tuple {item} is converted into single integer number : {int(x)}')

solution(sample)

