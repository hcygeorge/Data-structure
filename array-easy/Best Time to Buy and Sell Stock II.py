# Best Time to Buy and Sell Stock II

# Simple One Pass
# 只要明天價格比較高，就馬上賣策略
# 因為沒有限制進出次數和進出代價，這個方法雖然在嚴格遞增時會有多餘的操作，但還是能得到正解
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # count profit
        max_profit = 0
        
        # if price is larger than yesterday, sell it immediately
        for i in range(0, len(prices)):
            if i == 0:
                continue
            
            profit = prices[i] - prices[i-1]
            if profit > 0:
                max_profit += profit
                
        return max_profit
    
    
# Peak Valley
# 還沒答對
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # variables
        max_profit = 0
        valley = prices[0]
        peak = prices[0]
        
        # iterate
        for i in range(len(prices)-1):

            # find valley
            if prices[i] >= prices[i+1]:
                continue
            else:
                valley = prices[i]
                
            # find peak and count profit
            if prices[i] <= prices[i+1]:
                continue
            else:
                peak = prices[i]

            max_profit += peak - valley
            
            
        return max_profit
                