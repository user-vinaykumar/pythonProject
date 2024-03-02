# python program to compute the sum of all the tuples and store it in the list.

# [(1, 2), (2, 3), (3, 4)]
# Sum of all the elements of each tuple stored inside the said list of tuples:
# [3, 5, 7]

sample = [(1, 2), (2, 3), (3, 4)]

output = [(j[0] + j[1]) for j in sample]
print(output)


def test(item):
    out = map(sum, item)
    print(f'the output is : {list(out)}')

test(sample)

