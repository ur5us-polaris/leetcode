# Using temp string
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) == 0:
#             return 0
#         max_len: int = 1
#         head = 0
#         curr = 1
#         while curr < len(s):
#             temp_s = s[head:curr]
#             if s[curr] in temp_s:
#                 head = head + temp_s.index(s[curr]) + 1
#             curr += 1
#             max_len = max(max_len, curr - head)
#         return max_len

# Using dict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_len: int = 1
        head = 0
        curr = 1
        temp_dict = {s[head]: 0}
        while curr < len(s):
            if s[curr] in temp_dict:
                head = max(head, temp_dict[s[curr]] + 1)
            temp_dict[s[curr]] = curr
            curr += 1
            max_len = max(max_len, curr - head)
        return max_len


cases = [
    'abcabcbb',     # Expected 3
    'tmmzuxt',      # Expected 5
    'abbdac',         # Expected 4
    'aa',           # Expected 1
    'au',           # Expected 2
    'a',            # Expected 1
    ''              # Expected 0
]
sol = Solution()
for s in cases:
    print(f'{s}: {sol.lengthOfLongestSubstring(s)}')