# Straightforward solution
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         num = 0
#         i = 0
#         while i < len(s):
#             if s[i] == 'I':
#                 if i + 1 < len(s):
#                     if s[i+1] == 'V':
#                         num += 4
#                         i += 2
#                         continue
#                     if s[i+1] == 'X':
#                         num += 9
#                         i += 2
#                         continue
#                 num += 1
#             elif s[i] == 'X':
#                 if i + 1 < len(s):
#                     if s[i + 1] == 'L':
#                         num += 40
#                         i += 2
#                         continue
#                     if s[i + 1] == 'C':
#                         num += 90
#                         i += 2
#                         continue
#                 num += 10
#             elif s[i] == 'C':
#                 if i + 1 < len(s):
#                     if s[i + 1] == 'D':
#                         num += 400
#                         i += 2
#                         continue
#                     if s[i + 1] == 'M':
#                         num += 900
#                         i += 2
#                         continue
#                 num += 100
#             elif s[i] == 'V':
#                 num += 5
#             elif s[i] == 'L':
#                 num += 50
#             elif s[i] == 'D':
#                 num += 500
#             elif s[i] == 'M':
#                 num += 1000
#
#             i += 1
#         return num

# Cleaner solution
composite_letter_to_value = {
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}
letter_to_value = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        i = 0
        while i < len(s):
            letter = s[i]
            if i + 1 < len(s) and letter+s[i+1] in composite_letter_to_value:
                num += composite_letter_to_value[letter+s[i+1]]
                i += 2
                continue
            num += letter_to_value[letter]
            i += 1
        return num


s = 'III'
sol = Solution()
print(sol.romanToInt(s))
