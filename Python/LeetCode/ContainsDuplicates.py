from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()

        for num in nums:
            if num in nums_set: 
                return True
            else:
                nums_set.add(num)
        return False
    
s = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
print(s.containsDuplicate(nums))