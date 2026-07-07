class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 ## buy (should be low)
        r = 1 ## sell (should be high)
        maxP = 0
        while r < len(prices):
            if (prices[l] < prices[r]):
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r ## update the low to new low
            r+=1
        return maxP
