# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Create a pointer to head and attach lowest head of linked list

        Time Complexity: O(n)
        Space Complexity: O(1) max size wont go beyond 26 lowercase english chars
        """

        if not list1:
            return list2
        if not list2:
            return list1

        current = ListNode() # new empty node
        initial = current # head pointer

        while(list1 and list2):
            if list1.val <= list2.val:
                current.next = list1 # point current to next
                list1 = list1.next # move list1 pointer

            else:
                current.next = list2 
                list2 = list2.next

            current = current.next # move current pointer

        # worst case 1 is left?
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return initial.next
        