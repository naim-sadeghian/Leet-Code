class Solution:
    """
    Binary search look at middle and next element to see if we are in the ascending 
    or descending side. 
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while(left < right):
            mid = (left + right) >> 1
            if nums[mid] > nums[mid+1]:
                #descending: peak is to the left
                right = mid
            else:
                left = mid+1
        return left