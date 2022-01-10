from typing import List

# Two binary searches solution
class Solution:
    def look_for_left(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        left_boundry = len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid < left_boundry:
                    left_boundry = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left_boundry if left_boundry < len(nums) else -1

    def look_for_right(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        right_boundry = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid > right_boundry:
                    right_boundry = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return right_boundry

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.look_for_left(nums, target)
        right = self.look_for_right(nums, target)
        return [left, right]


# nums = [5,7,7,8,8,8,10]
# nums = []
nums = [1]

target = 1
s = Solution()
print(s.searchRange(nums, target))