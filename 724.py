class Solution:
    """
    Add and remove from right and left side and break if they
    are the same sum

    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        ans = -1
        for x in range(len(nums)):
            right -= nums[x]
            if (left == right):
                ans = x
                break
            left += nums[x]
        return ans