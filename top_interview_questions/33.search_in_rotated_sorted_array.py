from typing import List


class Solution:
    def find_pivot(self, nums: List[int], left, right):
        if left == right:
            return left

        # Deal with sorted lists, including lists with length of 1
        if nums[0] <= nums[len(nums) - 1]:
            return 0

        # Deal with lists having with length of 2
        if len(nums) == 2:
            return 1

        mid = (left + right) // 2
        if nums[mid] < nums[mid - 1]:
            return mid
        if nums[mid + 1] < nums[mid]:
            return mid + 1
        if nums[left] <= nums[mid]:
            return self.find_pivot(nums, mid + 1, right)
        else:
            return self.find_pivot(nums, left, mid - 1)

    def search(self, nums: List[int], target: int) -> int:
        pivot = self.find_pivot(nums, 0, len(nums) - 1)
        # We can do this in place, but for readability, we modify the given list
        nums = nums[pivot:] + nums[:pivot]
        # nums is now a sorted list, we can perform a binary search
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return (pivot + mid) % len(nums)
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


s = Solution()
# nums = [4, 5, 6, 7, 0, 1, 2]
# nums = [4, 0, 1, 2, 3]
# nums = [1]
# nums = [0, 1, 2]
# nums = [3,1]
nums = [3, 5, 1]
target = 1

print(s.search(nums, target))
