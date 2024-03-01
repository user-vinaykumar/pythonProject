# replace the last value of the tuple.
#Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

sample = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

print([t[:-1] + (100, ) for t in sample])
