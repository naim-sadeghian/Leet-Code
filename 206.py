# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Save previous and next pointers to reverse list

    Time Complexity: O(n)
    Space Complexity: O(1) only pointer to previous and next
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        previous = None 
        next = None
        while(pointer):
            next = pointer.next
            pointer.next = previous
            previous = pointer
            pointer = next
        return previous