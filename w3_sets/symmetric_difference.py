# print the symmetric difference of the two sets.

sample = {'blue', 'yellow', 'green'}
sample2 = {'blue', 'green', 'pink'}

def symmetric_difference(item, item2):
    print(f'the symmetric difference of the sets are : {item.symmetric_difference(item2)}')

symmetric_difference(sample, sample2)