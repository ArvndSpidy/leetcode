"""
Revision number: 1

Description:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Notes:
Add two pointers for indices left:0 and right:1. Now check if the left index value is less than right index value.
check the difference between 2 values and update the profit. After that move the right index to check the profit again.
If at any point, left index value is greater than right index value then update the left index value with right index value and increment the right index, as we know that if right value is less than left value then that must be the smallest number. 
"""

class Solution:
    def maxProfit(self, prices:list[int]) -> int:
        l,r = 0,1
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                current_profit = prices[r] - prices[l]
                max_profit = max(max_profit,current_profit)
            else:
                l = r
            r += 1
        return max_profit

solution = Solution()
print(solution.maxProfit([7,1,5,6,3]))