
from typing import Optional, List


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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Iterate the list till the end
        # For each node, keep a pointer in an array
        # When iteration finished, go to nth - 1 from the end and set its next to nth + 1
        curr = head
        temp_list: List[ListNode] = []
        while curr:
            temp_list.append(curr)
            curr = curr.next
        if temp_list[len(temp_list)-n] == head:
            head = head.next
        else:
            temp_list[len(temp_list)-n-1].next = temp_list[len(temp_list)-n].next
        return head


builder = ListNodeListBuilder().append(1).append(2).append(3).append(4).append(5)
s = Solution()

curr = s.removeNthFromEnd(builder.head, 2)
while curr:
    print(curr.val)
    curr = curr.next