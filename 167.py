class Solution:
    """
    Since list is ordered, we can use 2 pointers (at both ends) and move the pointers in to find target
    

    Time Complexity: O(n) worst case both numbers are in the center and we iterate the whole array
    Space Complexity: O(1) only 2 pointers are created
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while(left < right):
            print(left,right)
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            #If value is above target, bring right pointer to next lower value
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return[-1,-1]