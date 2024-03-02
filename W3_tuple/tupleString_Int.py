# # convert the strings inside the tuple to integers.
#
# sample = (('333', '33'), ('1416', '55'))
#
# def stringToint(item):
#     value = []
#     for i in item:
#         res = str(i)
#         value.append(res)
#     finalValue = tuple(value)
#     return finalValue
#
#
# def solution(item):
#     lis = []
#     for i in item:
#         lis.append(stringToint(i))
#     finalOutput = tuple(lis)
#
#     print(f'the {item} where string is replaced with the integer value : {finalOutput}')
#
# solution(sample)
