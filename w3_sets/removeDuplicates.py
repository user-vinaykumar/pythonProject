# remove duplicates from the list of strings and return the unique list of strings.

sample = ['foo', 'bar', 'abc', 'foo', 'qux', 'bar', 'baz']

def removeDuplicates(item):
    setItem = set(item)
    return setItem

def solution(items):
    resultList = list(removeDuplicates(items))
    print(f'the original list of strings is : {items}')
    print(f'the unique set of strings in the original list'
          f'after removing duplicates is : {resultList}')

solution(sample)