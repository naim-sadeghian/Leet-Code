class Solution:
    """
    Use DFS to "flood" neighbors and change to color.
    CHanging color also helps us know which ones we have visited already

    Time Complexity: O(m*n) worst case means the whole matrix is the same color
    Space Complexity: O(1) editing mage in place
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initial_color = image[sr][sc]

        
        def dfs(i, j):
            m = len(image)-1
            n = len(image[0])-1
            if (image[i][j] == initial_color):
                image[i][j] = color #paint in color

                #spread by dfs to neighbors
                if (i < m):
                    dfs(i+1, j)
                if (i > 0):
                    dfs(i-1, j)
                if (j < n):
                    dfs(i, j+1)
                if (j > 0):
                    dfs(i, j-1)

        # We use painting to signify that a node has been visited
        # It doesnt make sense to paint same color
        if (initial_color != color):
            dfs(sr,sc)
        return image