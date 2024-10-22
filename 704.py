class Solution:
    """
    Your go to binary search

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while( left <= right):
            mid = (right+left) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
            print(left,right)
        return -1
                