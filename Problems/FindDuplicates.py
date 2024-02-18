# find the duplicate elements that are repeated more than once in a list.
# this programme is not dynamic only applicable to some problems and not all of them.

def findDupicates(nums):
    tortoise = nums[0]  # 1
    hare = nums[0]  # 1
    while True:
        tortoise = nums[tortoise]  # 4
        hare = nums[nums[hare]]  # 4
        if tortoise == hare:
            break

    ptr1 = nums[0]  # 1
    ptr2 = tortoise  # 4
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]  # 4
        ptr2 = nums[ptr2]  # 4

    return ptr1


print(findDupicates([10, 11, 13, 13, 14, 13, 15]))
