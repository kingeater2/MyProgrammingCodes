from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_index = 0
        sell_index = 1 
        length = len(prices)
        
        while sell_index < length:
    
            if prices[buy_index] < prices[sell_index]:
                
                profit = max(profit, prices[sell_index] - prices[buy_index])
               
            else:
                buy_index = sell_index
            
            sell_index += 1 
        return profit
    
s = Solution()

prices = [7,1,5,3,6,4]

print(s.maxProfit(prices))
