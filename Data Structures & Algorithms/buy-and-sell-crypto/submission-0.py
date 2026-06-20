class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        result = 0

        i = 0
        while i < len(prices) - 1:
            buy = prices[i]
            sell = max(prices[i + 1:])
            profit = sell - buy
            if profit > result:
                result = profit
            i+=1
        
        return result