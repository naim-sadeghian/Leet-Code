class Solution:
    """
    Dynamically update the cost of reaching each stair using the minimum cost of  
    reaching the 2 steps below

    Time Complexity: O(n) iterate through whole list
    Space Complexity: O(1) no new space used, as we overwrite list
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])