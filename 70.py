class Solution:
    """
    Memorize steps taken at each n and use previous 2 to calculate current
    Kind of like a fibonacci

    Time Complexity: O(n)
    Space Complexity: O(n) create list of size n 
    """
    def climbStairs(self, n: int) -> int:
        stairs = [1,2]
        for i in range(0, n):
            stairs.append(stairs[-1] + stairs[-2])
        return stairs[n-1]