class Solution:
    """
    Use binary search to find target or point to correct position

    Time Complexity: O(log n)
    Space Complexity: O(1) 
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while (left <= right):
            middle = (left + right) >> 1
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return left