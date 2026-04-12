class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        sum=0
        while right<len(prices):
            if prices[left]>prices[right]:
                left+=1
                continue
            total=prices[right]-prices[left]
            right+=1
            sum=max(sum,total)
        return sum