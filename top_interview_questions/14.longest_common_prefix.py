from typing import List


# Pythonic solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for i in range(len(strs[0])):
            lc = [s[i] if i < len(s) else None for s in strs]
            if not all(lc) or len(set(lc)) > 1:
                break
            if len(set(lc)) == 1:
                prefix += lc[0]
        return prefix


strs = ["a"]
s = Solution()
print(s.longestCommonPrefix(strs))
