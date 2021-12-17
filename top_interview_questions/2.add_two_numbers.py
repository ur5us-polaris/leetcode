# Definition for singly-linked list.
from typing import Optional, List


class NodeListBuilder:
    def __init__(self):
        self.first: ListNode = None
        self.last: ListNode = None

    def append(self, value):
        node = ListNode(value)
        if self.first is None:
            self.first = node
        if self.last is not None:
            self.last.next = node
        self.last = node
        return self



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = NodeListBuilder()
        carry: int = 0
        while l1 or l2 or carry:
            temp: int = carry
            if l1 is not None:
                temp += l1.val
                l1 = l1.next
            if l2 is not None:
                temp += l2.val
                l2 = l2.next
            carry, res_val = divmod(temp, 10)
            result.append(res_val)
        return result.first


# Node lists:
# l1 = [2, 4, 3]
# l2 = [5, 6, 4]
nl1 = NodeListBuilder().append(2).append(4).append(3)
nl2 = NodeListBuilder().append(5).append(6).append(4)

s = Solution()
res = s.addTwoNumbers(nl1.first, nl2.first)
while res is not None:
    print(res.val)
    res = res.next
