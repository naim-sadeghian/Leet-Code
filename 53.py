class Solution:
    """
    Kadane’s : Choose between adding number to sub-array sum or
    start new array using number 

    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0] #start with first as best
        best = nums[0] #start with first as best
        # ans = []
        for i in range(1,len(nums)):
            if sum + nums[i] > nums[i]:
                sum += nums[i]
                # ans.append(nums[i])
            else:
                sum = nums[i]
                # ans = [nums[i]]
            best = max(best, sum)
        return best