class Solution:
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        list_of_traversed = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in list_of_traversed:
                return [i, list_of_traversed[diff]]
            list_of_traversed[nums[i]] = i

solution = Solution()
print(solution.twoSum([3,2,4],6))