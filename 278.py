class Solution:
    """
    Your go to binary search

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    def firstBadVersion(self, n: int) -> int:
        right = n
        left = 0
        while(left <= right):
            mid = (left+right) >> 1
            if isBadVersion(mid) and (mid==0 or not(isBadVersion(mid-1))):
                return mid
            elif isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
            print(left,right)
        return left