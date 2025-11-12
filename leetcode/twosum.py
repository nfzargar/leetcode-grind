
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    mydict = {}
    for index, value in enumerate(nums):
        mydict[value] = index
    for i, x in enumerate(nums):
        y = target - x
        if y in mydict and mydict[y] != i:
            return [i,mydict[y]]

nums = [3,2,4] 
target = 6
print(twoSum(nums, target))