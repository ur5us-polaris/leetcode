from typing import List
from math import log10, floor

MAX = 2**31 - 1
MIN = -2**31


# Pythonic solution, pretty much cheating :)
# class Solution:
#     def reverse(self, x: int) -> int:
#         neg = 1 if x > 0 else -1
#         s_x = str(x * neg)[::-1]
#         rev_x = int(s_x) * neg
#         if rev_x > MAX or rev_x < MIN:
#             return 0
#         return rev_x



# Simple solution, breaking down and building up the int are seperated
# def int_to_list(x: int) -> List[int]:
#     rev_list = []
#     while x > 0:
#         x, rem = divmod(x, 10)
#         rev_list.append(rem)
#     rev_list.reverse()
#     return rev_list
#
#
# class Solution:
#     def reverse(self, x: int) -> int:
#         neg = 1 if x >= 0 else -1
#         rev_x = 0
#         for i, n in enumerate(int_to_list(x * neg)):
#             rev_x += n * 10**i
#         rev_x *= neg
#         if rev_x > MAX or rev_x < MIN:
#             return 0
#         return  rev_x

# Optimized solution, breaking down and building up the int are combined
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        neg = 1 if x > 0 else -1
        x *= neg
        rev_x = 0
        i = 0
        n = floor(log10(x))
        while x > 0:
            x, rem = divmod(x, 10)
            rev_x += rem * 10**(n - i)
            i += 1
        if rev_x > MAX or rev_x < MIN:
            return 0
        return rev_x * neg


x = -123
s = Solution()
print(s.reverse(x))
