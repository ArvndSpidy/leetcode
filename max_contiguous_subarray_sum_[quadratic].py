class Solution:
    def maxSubArray(self, nums:list[int]) -> int:
        n = len(nums)
        max_sum = -1000
        for left in range(0,n):
            running_sum = 0
            for right in range (left, n):
                running_sum += nums[right] 
                max_sum = max(max_sum, running_sum)  
        return max_sum

solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))