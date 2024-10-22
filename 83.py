# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Since the lsit is in order you can just move the head until it is different in value

    Time Complexity: O(n)
    Space Complexity: O(1) only pointer to next
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = head
        while(head):
            if (head.next and head.next.val == head.val): #iteratate until you reach a different val
                next = head.next
                while(next and next.val == head.val):
                    next = next.next
                head.next = next


            head = head.next
        return ans