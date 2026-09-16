class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        max_sell = 0
        for num in prices:
            buy = min(buy, num)
            sell = num - buy
            max_sell= max(sell, max_sell)
        return max_sell



        