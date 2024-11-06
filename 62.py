class Solution:
    """
    Save steps it takes to get to position i,j and check with previous cells (above and to the left) to find new total

    Time Complexity: O(n*m)
    Space Complexity: O(n*m) 
    """
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1] * m for _ in range(n)]
        for i in range(1,m):
            for j in range(1,n):
                matrix[j][i] = matrix[j-1][i] + matrix[j][i-1]
        return matrix[n-1][m-1]