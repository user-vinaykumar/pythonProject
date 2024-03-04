# Find the maximum product of all the numbers in the list.
# And return the pair of those numbers.

sample = [1,2,3,4,5,6,7,8,9,0]

def maxProduct(item):
    itemSet = set(item)

    max_product = 0
    max_num1 = None
    max_num2 = None

    for n1 in itemSet:
        for n2 in itemSet:
            if n1 != n2 and n1 * n2 > max_product:
                max_product = n1 * n2
                max_num1 = n1
                max_num2 = n2


    print(f'the maximum numbers for the maximum product are : {(max_num1, max_num2)}')
    print(f'the maximum product : {max_product}')

maxProduct(sample)




