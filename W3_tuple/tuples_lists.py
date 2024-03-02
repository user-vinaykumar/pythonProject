# python program to convert the tuples inside a list to a lists.

#Original list of tuples: [(1, 2), (2, 3), (3, 4)]
#Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]

sample = [(1, 2), (2, 3), (3, 4)]
sample2 =  [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]

def test(item):
    out = map(list, item)
    print(f'the output for the problem is : {list(out)}')

test(sample2)