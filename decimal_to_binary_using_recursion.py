class Solution:
    def decimalToBinary(self, decimal:int, result: str) -> str:
        if decimal == 0:
            return result
        result = str(decimal % 2) + result
        return self.decimalToBinary(decimal // 2, result)

solution = Solution()
print(solution.decimalToBinary(233, ''))