class Solution:
    """
    Throw a DFS in islands that haven't been visited and mark them all as 0
    First time starting a DFS will paint the whole island as 0
    Count Islands

    Time Complexity: O(n*m) iterate matrix 
    Space Complexity: O(1) edit matrix in-place
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = {}
        ans = 0
        for i in range(len(grid)):
           for j in range(len(grid[0])):
               if grid[i][j] == "1":
                   ans += 1
                   self.bfs(i, j, grid)
        return ans
                   


    def bfs(self, row, column, grid):
        if row > 0:
            if grid[row-1][column] == "1":
                grid[row-1][column] = "0"
                self.bfs(row-1, column, grid)

        if row < len(grid)-1:
            if grid[row+1][column] == "1":
                grid[row+1][column] = "0"
                self.bfs(row+1, column, grid)

        if column > 0:
            if grid[row][column-1] == "1":
                grid[row][column-1] = "0"
                self.bfs(row, column-1, grid)

        if column < len(grid[0])-1:
            if grid[row][column+1] == "1":
                grid[row][column+1] = "0"
                self.bfs(row, column+1, grid)

        