class Solution:
    def validAnagram(self, s:str, t:str) -> bool:
        s_counts, t_counts = {},{}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_counts[s[i]] = 1 + s_counts.get(s[i], 0)
            t_counts[t[i]] = 1 + t_counts.get(t[i], 0)
        for c in s:
            if s_counts[c] != t_counts.get(c, 0):
                return False
        return True
        
solution = Solution()
print(solution.validAnagram('anagram','nagaram'))