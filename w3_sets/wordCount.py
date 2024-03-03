# print the word count of the word present in the set.
import lists

sample = ['red', 'green', 'black', 'red', 'red', 'black', 'purple', 'black', 'purple', 'purple']

def wordsCount(item):
    sampleSet = set(item)
    word_count = {}

    for word in sampleSet:
        word_count[word] = item.count(word)

    return word_count

def solution(items):
    print(f'the word count of {items} are : \n {wordsCount(items)}')

solution(sample)
