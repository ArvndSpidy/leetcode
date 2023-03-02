class Solution:
    def stringReversal(self, s:str) -> str:
        if s == "":
            return ""
        return self.stringReversal(s[1:]) + s[0]

solution = Solution()
print(solution.stringReversal("hello, world"))