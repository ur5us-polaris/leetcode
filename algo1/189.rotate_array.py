# Extend method is used since we need to modify the list in-place.
# That's wasteful, because it made us use a helper list and not achieve O(1) of space.
# If the caller's arguments were given to us, we could use globals to change the list in-place:
# global()['list_arg_name'] = nums[(n - k) % n:] + nums[:(n - k) % n]

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = nums.copy()
        n = len(nums)
        nums.clear()
        nums.extend(temp[(n - k) % n:])
        nums.extend(temp[:(n - k) % n])


def main():
    nums = [-1, -100, 3, 99]
    k = 2
    s = Solution()
    s.rotate(nums, k)
    print(nums)


if __name__ == '__main__':
    main()
