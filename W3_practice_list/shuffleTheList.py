# shuffle the list and print the list
import random

sample = [1,2,3,4,5,6,7,8,9,10]

# first approach

def shuffle(item):
    shuffleList = set(item)
    newList = list(shuffleList)
    print(newList)

shuffle(sample)

print('---------------------')

# second approach

from random import shuffle

def shuffleSecond(item):
    random.shuffle(item)
    print(item)

shuffleSecond(sample)

