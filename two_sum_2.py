
class Solution:
    def twoSum2(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return []
    
solution = Solution()
print(solution.twoSum2([2,7,11,15], 9))