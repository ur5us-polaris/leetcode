from typing import List
from math import floor

# O(nlogn) solution
# def binary_search(numbers: List[int], target: int) -> int:
#     left = 0
#     right = len(numbers) - 1
#     while left <= right:
#         mid = floor((left + right) / 2)
#         if numbers[mid] == target:
#             return mid
#         if numbers[mid] < target:
#             left = mid + 1
#         elif numbers[mid] > target:
#             right = mid - 1
#     return -1
#
#
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i, n in enumerate(numbers):
#             diff = target - n
#             index = binary_search(numbers[:i] + numbers[i + 1:], diff)
#             if index != -1:
#                 return [i + 1, index + 2]


# O(n) solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1



numbers = [-1,0]
target = -1
s = Solution()
print(s.twoSum(numbers, target))

