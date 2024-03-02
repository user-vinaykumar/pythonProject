# adding the sequential elements of different tuples and storing the answers
# in different tuple.
# (1, 2, 3, 4)
# (3, 5, 2, 1)
# (2, 2, 3, 1)
# Element-wise sum of the said tuples:
# (6, 9, 8, 6)

sample1 = (1, 2, 3, 4)
sample2 = (3, 5, 2, 1)
sample3 = (2, 2, 3, 1)


def solution(item1, item2, item3):
    result = []
    for i in range(len(item1)):
        output = item1[i] + item2[i] + item3[i]
        result.append(output)
    finalResult = tuple(result)
    print(f'the output of the problem is : {finalResult}')

solution(sample1, sample2, sample3)
