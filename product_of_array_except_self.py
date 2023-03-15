"""
Revision number: 1

Description:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Notes:
First calculate the prefix of each value and store in a list. for ex: if the input is 1,2,3,4 then after the first pass the result list would be 1,1,2,6. Then make a second pass and calculate the postfix and multiply it with the result list.

Time Complexit: O(n)
we iterate the list only once.
Space Complexity:O(1)


"""
class Solution:
    def productExceptSelf(self, nums:list[int]) -> list[int]:
        res = [1] * len(nums)
        prefix = postfix = 1
        for i in range(len(nums)):
           res[i] = prefix
           prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
           res[i] *= postfix
           postfix *= nums[i]
        return res   
    
solution = Solution().productExceptSelf([1,2,3,4])
print(solution)