from typing import Optional


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


# New list solution
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         new_list_builder = ListNodeListBuilder()
#         while list1 or list2:
#             if not list1:
#                 new_list_builder = new_list_builder.append(list2.val)
#                 list2 = list2.next
#             elif not list2:
#                 new_list_builder = new_list_builder.append(list1.val)
#                 list1 = list1.next
#             elif list2.val <= list1.val:
#                 new_list_builder = new_list_builder.append(list2.val)
#                 list2 = list2.next
#
#             elif list1.val < list2.val:
#                 new_list_builder = new_list_builder.append(list1.val)
#                 list1 = list1.next
#         return new_list_builder.head

# In place solution, very messy
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         head = None
#         tail = None
#         if list1 and list2:
#             if list1.val < list2.val:
#                 head = tail = list1
#                 list1 = list1.next
#             else:
#                 head = tail = list2
#                 list2 = list2.next
#         elif list1 and not list2:
#             head = tail = list1
#             list1 = list1.next
#         elif list2 and not list1:
#             head = tail = list2
#             list2 = list2.next
#
#         while list1 or list2:
#             if list1 and not list2:
#                 tail.next = list1
#                 tail = tail.next
#                 list1 = list1.next
#             elif list2 and not list1:
#                 tail.next = list2
#                 tail = tail.next
#                 list2 = list2.next
#             elif list1.val < list2.val:
#                 tail.next = list1
#                 tail = tail.next
#                 list1 = list1.next
#             else:
#                 tail.next = list2
#                 tail = tail.next
#                 list2 = list2.next
#
#         return head

# In place recursive solution
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val > list2.val:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        else:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1

list1 = ListNodeListBuilder().append(1).append(2).append(4)
list2 = ListNodeListBuilder().append(1).append(3).append(4)
s = Solution()
merged = s.mergeTwoLists(list1.head, list2.head)
while merged:
    print(merged.val)
    merged = merged.next