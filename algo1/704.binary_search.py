from math import floor
from typing import List


def search(nums: List[int], target: int) -> int:
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
    return -1


def main():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    res = search(nums, target)
    print(res)


if __name__ == '__main__':
    main()

