# find the duplicate elements that are repeated more than once in a list.

def findDupicates(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1


print(findDupicates([1, 2, 3, 4, 4, 5, 2, 4, 9, 2, 1, 6, 7]))
