from typing import List

# Suboptimal, O(n+m)
def merge_sorted_sort(list_a: List[int], list_b: List[int]) -> List[int]:
    result_list = []
    i = 0
    j = 0
    while i < len(list_a) or j < len(list_b):
        if j >= len(list_b):
            return result_list + list_a[i:]
        if i >= len(list_a):
            return result_list + list_b[j:]
        if list_a[i] > list_b[j]:
            result_list.append(list_b[j])
            j += 1
        else:
            result_list.append(list_a[i])
            i += 1
    return result_list


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final_list = merge_sorted_sort(nums1, nums2)
        mid = len(final_list) // 2
        if not len(final_list) % 2:
            return (final_list[mid - 1] + final_list[mid]) / 2
        return final_list[mid]


list_a = [1,2]
list_b = [3,4]
s = Solution()
print(s.findMedianSortedArrays(list_a, list_b))

