class Solution:
    def sumOfNaturalNumbers(self,num:int) -> int:
        if num == 1:
            return num
        return num + self.sumOfNaturalNumbers(num - 1)
    
solution = Solution()
print(solution.sumOfNaturalNumbers(55))