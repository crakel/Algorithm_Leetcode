import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = sys.maxsize
        
        for price in prices:
            min_price = min(min_price, price)          
            max_profit = max(max_profit, price - min_price)
        return max_profit
    
        # 슬라이싱 활용 -> 시간초과
        # max_profit = 0
        # for i in range(len(prices)-1):
        #   buy = prices[i]
        #   sell_list = prices[i+1:]
        #   max_profit = max(max_profit, max(sell_list)-buy)
        
        # return max_profit
        
        # 브루트포스 -> 시간초과
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         max_profit = max(max_profit, prices[j] - prices[i])
        # return max_profit