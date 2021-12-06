from math import floor
from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = floor((right + left) / 2)
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
            continue
        if nums[mid] > target:
            right = mid - 1
    return right + 1


def main():
    nums = [1, 2, 3, 5, 7, 9]
    target = 11
    res = searchInsert(nums, target)
    print(res)


if __name__ == '__main__':
    main()