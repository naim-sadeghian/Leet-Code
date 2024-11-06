"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    """
    Time Complexity: O(n^2 * log n) binary search mixed with matrix brute search
    Space Complexity: O(log n) we are divideing the matrix into quarters. If there was a case with alternating 0 1 0 1...
                               then the complexity would be n^2  
    """
    def construct(self, grid: List[List[int]]) -> 'Node':

        def quad(i, j, n) -> 'Node':

            row = i
            same = True
            if n == 1:
                print(i,j)
                return Node(grid[i][j], 1, None, None, None, None)

            #Check if all are the same in that quadrant
            while row < i + n and same:
                for col in range(j, j + n):
                    if grid[row][col] != grid[i][j]:
                        same = False
                        break
                row += 1

            if not same:
                tl = quad(i, j, (n>>1))
                tr = quad(i, j+(n>>1) , (n>>1))
                bl = quad(i+(n>>1), j, (n>>1))
                br = quad(i+(n>>1), j+(n>>1) , (n>>1))
                return Node(1, 0, tl, tr, bl, br)
            else:
                return Node(grid[i][j], 1, None, None, None, None)

        return quad(0,0,len(grid))