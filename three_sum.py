"""
Revision number: 1

Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Notes:
First complete two sum and two sum II problems.
Sort the list of nums. After sorting use a for loop to traverse each element(a) for 1 time and use two pointers l and r at index 0 and len(input) - 1. add the a,l value and r value to check if they sums up to 0 and append it to a list if thats true. if not, change l and r places and check again. repeat till l < r. check the l and its next value should not be same. r and its prev value should not be changed.

Time Complexit:O(n^2)
n - for loop
n - traversing two pointers
 
Space Complexity:
n - we do sorting initially.

"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l,r = i + 1, len(nums) - 1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
        return res

solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))