class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp = nums.copy()
        n = len(nums)
        last0 = 0
        for curr in range(0, n):
            if temp[curr] != 0:
                temp[curr], temp[last0] = 0, temp[curr]
                last0 += 1
        nums.clear()
        nums.extend(temp)


def main():
    nums = [0,1,0,3,12]
    s = Solution()
    s.moveZeroes(nums)
    print(nums)


if __name__ == '__main__':
    main()
