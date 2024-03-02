# python program to intersect the sets.

sample = {'mandya', 'bengaluru', 'mysuru', 'tumakuru'}
sample2 = {'karnataka', 'kerala', 'goa', 'bengaluru', 'mysuru'}



def setIntersection(item, item2):
    print(f'the intersection of sets : {item.intersection(item2)}')

setIntersection(sample, sample2)