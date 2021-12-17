from typing import List

# Brute force solution with O(n^3) complexity
# def get_all_substrings(s: str) -> List[str]:
#     substrings = []
#     for i in range(len(s)):
#         for j in range(i + 1, len(s)+1):
#             substrings.append(s[i: j])
#     return substrings
#
#
# def is_palindrome(s: str) -> bool:
#     for i in range(len(s) // 2):
#         if s[i] != s[len(s) - i - 1]:
#             return False
#     return True
#
#
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) <= 1:
#             return s
#         longest_palindrome = ''
#         print(get_all_substrings(s))
#         for substring in get_all_substrings(s):
#             if is_palindrome(substring):
#                 if len(substring) > len(longest_palindrome):
#                     longest_palindrome = substring
#         return longest_palindrome


# Expand around center solution, probably O(n^2) complexity?
def expand_until_not_palindrome(s: str, left: int, right: int) -> int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        pal_start = 0
        pal_end = 0
        for i in range(len(s)):
            len_odd = expand_until_not_palindrome(s, i, i)
            len_even = expand_until_not_palindrome(s, i, i + 1)
            pal_len = max(len_odd, len_even)
            if pal_len > pal_end - pal_start:
                pal_start = i - (pal_len-1) // 2
                pal_end = i + pal_len // 2
                print(f'{pal_start=}')
                print(f'{pal_end=}')
        return s[pal_start: pal_end+1]


# s = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
s = 'abjbajjjjjjb'
sol = Solution()
print(sol.longestPalindrome(s))