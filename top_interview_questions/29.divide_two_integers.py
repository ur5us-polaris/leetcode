

MIN = -2**31
MAX = 2**31 - 1


def clamp(val) -> int:
    if val < MIN:
        return MIN
    if val > MAX:
        return MAX
    return val


# Subtraction solution
# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         sign = 1 if dividend * divisor >= 0 else -1
#         dividend = abs(dividend)
#         divisor = abs(divisor)
#         if divisor == 1:
#             return clamp(dividend * sign)
#         res = 0
#         while dividend >= divisor:
#             res += 1
#             dividend -= divisor
#             print(res)
#         return self._clamp(res * sign)


# A faster, more complex solution, using bitshift
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1 if dividend * divisor >= 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if divisor == 1:
            return clamp(dividend * sign)
        res = 0
        temp_divisor = divisor
        while temp_divisor <= dividend:
            temp_divisor = temp_divisor << 1
            if res == 0:
                res = 1
            else:
                res = res << 1
        if res == 0:
            return 0
        return clamp((res + self.divide(dividend - (temp_divisor >> 1), divisor)) * sign)


s = Solution()
print(s.divide(10, 3))
print(s.divide(-7, 3))
print(s.divide(-2147483648, -1))
print(s.divide(2147483647, 2))
print(s.divide(800, 2))



