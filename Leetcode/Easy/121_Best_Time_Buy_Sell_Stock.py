class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = 1
        maxProfit = 0 
        while right < len(prices):
            curProfit = prices[right] - prices[left]
            if prices[left] >= prices[right] :
                left = right
            else :
                maxProfit = max(maxProfit,curProfit)
            right += 1
        return maxProfit
            
