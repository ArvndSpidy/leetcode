"""
Revision number: 

Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Notes:
traverse each item and calculate the difference between the target and item. check if that item is in hashmap stored its index as value. If it is not there then store the traversed item with its index.

Time Complexit: O(n)
we might traverse till the end of the list.
Space Complexity:O(n)
since we are using an additional hashmap


"""
class Solution:
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        lookup = {}
        for i in range(len(nums)):
            diff = target - nums[i] 
            if diff in lookup:
                return [lookup[diff],i]
            else:
                lookup[nums[i]] = i
solution = Solution()
print(solution.twoSum([3,2,4],6))