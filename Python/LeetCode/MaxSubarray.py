from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MaxSum = nums[0]
        CurSum = 0
        
        for num in nums:
            if CurSum < 0: 
                CurSum = 0
            CurSum += num
            MaxSum = max(CurSum, MaxSum)
            
        return MaxSum
s = Solution()

nums = [-1]
print(s.maxSubArray(nums))