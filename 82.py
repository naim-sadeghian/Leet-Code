# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    2 pointers, prev pointer will stay behind while current iterates over repeated until there is none 
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current:

            if current.next and current.val == current.next.val:
                duplicate = current.val
                current = current.next
                while current and current.val == duplicate:
                    current = current.next

                if prev == None:
                    head = current # point to new head
                else: 
                    prev.next = current # link to new unrepeated

            else:
                prev = current
                current = current.next

        return head

        
        