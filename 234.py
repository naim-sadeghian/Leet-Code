# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     """
    This is the space efficient answer as it is more interesting.
    Used a slow and fast pointer to find the middle of the list and
    invert the second half.
    Iterate both ends and compare.

    Time Complexity: O(n) 
    Space Complexity: O(1)
    """
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        #get fast to end so that slow will be in the middle
        while fast != None and fast.next != None:
            fast = fast.next.next 
            slow = slow.next
        
        #invert second half
        prev = None
        nex = None
        while slow:
            nex = slow.next
            slow.next = prev
            prev = slow
            slow = nex
        
        #compare starting from both ends
        left = head
        right = prev
        while left and right and left != right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next
        return True 
