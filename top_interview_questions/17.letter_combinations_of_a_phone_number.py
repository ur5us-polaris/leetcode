import itertools
from typing import List
from copy import copy


digits_to_letters = [
    ' ',
    None,
    'abc',
    'def',
    'ghi',
    'jkl',
    'mno',
    'pqrs',
    'tuv',
    'wxyz'
]
# Semi-pythonic way: implementation of cartesian product
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         combinations = []
#         for digit in digits:
#             letters = digits_to_letters[int(digit)]
#             print(f'{letters=}')
#             if not len(combinations):
#                 for letter in letters:
#                     combinations.append(letter)
#                     print(f'{combinations=}')
#             else:
#                 temp_combs = []
#                 for letter in letters:
#                     cp = copy(combinations)
#                     temp_combs += [c + letter for c in cp]
#                 combinations = temp_combs
#         return combinations

# Fully-pythonic way: using itertools.product function for cartesian product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        num_list = [digits_to_letters[int(i)] for i in list(digits)]
        combs_lists = list(itertools.product(*num_list))
        combinations = []
        for each in combs_lists:
            combinations.append(''.join(list(each)))
        return combinations

s = Solution()
digits = '234'
print(s.letterCombinations(digits))
