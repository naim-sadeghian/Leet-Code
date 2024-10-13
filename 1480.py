class Solution:
    """
    Time Complexity: O(N)
    Space Complexity: O(1) im working on the same list
    """
    def runningSum(self, nums: List[int]) -> List[int]:
        # Basic for loop answer
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums