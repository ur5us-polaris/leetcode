from typing import List


# Naive O(n^2) solution
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i, n1 in enumerate(nums):
#             for j, n2 in enumerate(nums[:i] + nums[i + 1:]):
#                 if n1 + n2 == target:
#                     return [i, j + 1]

# O(n) solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, n in enumerate(nums):
            n2 = hash_map.get(n, None)
            if n2 is not None:
                return [i, n2]
            hash_map[target - n] = i


nums = [2, 7, 11, 15]
target = 26
s = Solution()
print(s.twoSum(nums, target))
