from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_dict = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in nums_dict: 
                return [nums_dict[complement], index]
            else:
                nums_dict[num] = index
        return
s = Solution()

nums = [3,2,4]
target = 6
print(s.twoSum(nums, target))
                
        
        
        