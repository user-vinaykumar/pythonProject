# find the third largest number from a given list of numbers.

sample = [11,12,13,14,15,16,17,18,19]

def third_Largest(item):
    item.remove(max(item))
    item.remove(max(item))
    print(f'the third largest number in the setList is {(max(item))}')

third_Largest(sample)