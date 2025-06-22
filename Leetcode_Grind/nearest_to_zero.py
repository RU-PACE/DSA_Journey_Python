# from typing import List
#
#
# class Solution:
#     def findClosestNumber(self, nums: List[int]) -> int:
#         nums = [abs(x) for x in nums]
#         nums.sort()
#         print(nums[0])
#
#
# Solution.findClosestNumber(None, [-1,-4,-9,-34,7,9,67])

from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:

        closest = nums[0]
        for i in nums:
            if abs(i) < abs(closest):
                closest = i
        print(closest)

        if closest < 0 and abs(closest) in nums:
            print(abs(closest))
        else:
            print(closest)


Solution.findClosestNumber(None, [-1,-4,-9,-34,7,9,67,1])
