class Solution:
    """
    Follow path for each ball and check if it doesn't leave bounds or crach against an oposing path

    Time Complexity: O(n^2)
    Space Complexity: O(n) ans is array of size columns 
    """
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = [0]*len(grid[0])
        for col in range(0, len(grid[0])):
            current = col
            for row in range(0, len(grid)):
                nextCol = current + grid[row][current]
                if(nextCol < 0 or nextCol == len(grid[0]) or grid[row][current] != grid[row][nextCol]):
                    ans[col] = -1
                    break
                ans[col] = nextCol
                current = nextCol
        return ans

