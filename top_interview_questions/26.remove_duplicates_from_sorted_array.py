from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        currlen = len(nums) - 1
        i = 0
        while i < currlen:
            if nums[i+1] == nums[i]:
                del(nums[i+1])
                currlen -= 1
                continue
            i += 1
        return len(nums)


array = [1, 2, 2, 7, 9, 9, 9, 9, 11, 11]
s = Solution()
k = s.removeDuplicates(array)
print(k)
print(array)