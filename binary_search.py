class Solution:
    def binarySearch(self,nums: list[int], left: int, right: int, key:int) -> int:
        if left > right:
            return -1
        
        mid = int((left + right) / 2)

        if key == nums[mid]:
            return mid
        if key < nums[mid]:
            return self.binarySearch(nums, left, mid - 1, key)
        return self.binarySearch(nums, mid + 1, right, key)
    
solution = Solution()
print(solution.binarySearch([0,1,2,3,4,5,6], 0, 6, 1))