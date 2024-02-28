# print the frequency of the elements in a list.

sample = [10, 10, 10, 20, 20, 20, 30, 30, 40, 50, 50]



def dictionary(item):
    sampleDictionary = {}
    for i in item:
        sampleDictionary[i] = sampleDictionary.get(i, 0)+1
    return sampleDictionary

def solution(matter):
    print(f'the frequency of the elements in the list are : {dictionary(matter)}')

solution(sample)
