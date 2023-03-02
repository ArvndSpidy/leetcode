class Solution:
    def containsDuplicate(self, nums:list[int]) -> bool:
        lookup = {}
        for number in nums:
            if number in lookup:
                return True
            lookup[number] = 1
        return False 
    
solution = Solution()
print(solution.containsDuplicate([1,2,3,4,1]))