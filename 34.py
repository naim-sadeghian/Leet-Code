class Solution:
     """
    Modified binary search to find first and last ocurance:
    - lower: searches for first target
    - higher: searcher for last target appearance

    Time Complexity: O(log n)
    Space Complexity: O(1) 
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or target < nums[0] or target > nums[-1]:
            return [-1,-1]
        left, right = 0, len(nums) -1
        if nums[left] == target == nums[right]:
            return [left, right]
        return [self.lower(nums, target), self.higher(nums, target)]

    def lower(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) >> 1
            if nums[middle] == target:
                if middle == 0 or nums[middle-1] != target:
                    return middle
                else:
                    right = right - 1
            else:   
                if nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1
    def higher(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) >> 1
            if nums[middle] == target:
                if middle == len(nums)-1 or nums[middle+1] != target:
                    return middle
                else:
                    left = middle + 1
            else:
                if nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1
        