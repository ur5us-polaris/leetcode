from math import floor, log10

ORD_0 = ord('0')
MAX = 2**31 - 1
MIN = -2**31

class Solution:
    def myAtoi(self, s: str) -> int:
        final = 0
        start = 0
        # Ignore leading whitespaces
        for start in range(len(s)):
            if s[start] != ' ':
                break
        # Check for sign
        sign = 1
        if start < len(s) and s[start] in '-+':
            sign = -1 if s[start] == '-' else 1
            start += 1
        # Ignore leading 0s
        for i, char in enumerate(s[start:]):
            if char != '0':
                start += i
                break
        # Start converting
        final = 0
        for i, char in enumerate(s[start:]):
            if char in '0123456789':
                final = final*10 + (ord(char) - ORD_0)
            else:
                break
        final *= sign
        # Clamp and return result
        return max(min(final, MAX), MIN)


s = '21474836460'
sol = Solution()
print(sol.myAtoi(s))
7