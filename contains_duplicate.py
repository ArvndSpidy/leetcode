"""
Revision number: 1

Description:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Notes:
Take a hashmap and start traversing the list. For every traversal check if the number is in hashmap or not. If the number does not exist then add the number to the hashmap. If exists return True. Outside the loop return False.

Time Complexit: O(n)
we iterate the list only once.
Space Complexity:O(n)
We store the values in hashmap for checking.

"""

class Solution:
    def containsDuplicate(self, nums:list[int]) -> bool:
        lookup = {}
        for num in nums:
            if num in lookup:
                return True
            lookup[num] = 1
        return False
    
solution = Solution()
print(solution.containsDuplicate([1,2,3,4,5]))
print(solution.containsDuplicate([1,2,3,4,1]))