from collections import Counter
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        local_nums = sorted(nums)
        three_sums = []
        used_a = set()
        for i, n in enumerate(local_nums):
            print(f'Dealing with {n}')
            if n > 0:
                break
            if n in used_a:
                continue
            left = i + 1
            right = len(local_nums) - 1
            while left < right:
                print(f'{left=}, {right=}')
                temp_sum = n + local_nums[left] + local_nums[right]
                if temp_sum == 0:
                    three_sums.append([n, local_nums[left], local_nums[right]])
                    used_a.add(n)
                    left += 1
                    while local_nums[left] == local_nums[left-1] and left < right:
                        left += 1
                if temp_sum > 0:
                    right -= 1
                elif temp_sum < 0:
                    left += 1
        return three_sums


nums = [-1,0,1,2,-1,-4]
# nums = []
# nums = [0,0,0,0,0]
s = Solution()
print(s.threeSum(nums))
