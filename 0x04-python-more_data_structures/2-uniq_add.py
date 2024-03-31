#!/usr/bin/python3
def uniq_add(my_list=[]):
    nums = {}
    sum = 0
    for num in my_list:
        nums[num] = 1
    for item in nums:
        sum += item
    return sum
