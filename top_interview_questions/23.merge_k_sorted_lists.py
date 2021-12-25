from typing import List, Optional
from math import inf


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNodeListBuilder:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val=0):
        node = ListNode(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        return self


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged_array = []
        for l in lists:
            while l:
                merged_array.append(l.val)
                l = l.next
        b = ListNodeListBuilder()
        for n in sorted(merged_array):
            b.append(n)
        return b.head


lists = []
arrays = [
    [1, 3, 4, 7],
    [2, 2, 5, 6, 13],
    [1, 92]
    ]

for array in arrays:
    b = ListNodeListBuilder()
    for a in array:
        b.append(a)
    lists.append(b.head)

for i, l in enumerate(lists):
    print(f'list {i}:')
    curr = l
    while curr:
        print(curr.val, end=' ')
        curr = curr.next
    print()

s = Solution()
merged = s.mergeKLists(lists)
curr = merged
while curr:
    print(curr.val, end=' ')
    curr = curr.next
