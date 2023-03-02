class Solution:
    def isPallindrome(self,s:str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True
        if s[0] == s[-1]:
            return self.isPallindrome(s[1:-1])
        return False
solution = Solution()
print(solution.isPallindrome("madam"))