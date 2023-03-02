class Solution:
    def maxSubArray(self, nums:list[int]) -> int:
        n = len(nums)
        max_sum = -1000
        for left in range(0,n):
            for right in range (left, n):
                window_sum = 0
                for k in range(left, right + 1):
                    window_sum += nums[k]
                max_sum = max(max_sum, window_sum)  
        return max_sum

solution = Solution()

print(solution.maxSubArray( [-2,1,-3,4,-1,2,1,-5,4]))