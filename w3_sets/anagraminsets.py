# # write a python program to find all the anagrams and group them together from a
# # given list of strings
#
# sample = ['eat', 'cba', 'tae', 'xyz']
#
#
# def sol(item):
#     result = {}
#     for i in item:
#         sorted_word = ''.join(sorted(i))
#         if sorted_word in result:
#             result[sorted_word].append(i)
#         else:
#             result[sorted_word] = i
#
#
#     print(f'the original list of string : {item}')
#     print(f'the anagram list : {list(result.values())}')
#
#
# sol(sample)