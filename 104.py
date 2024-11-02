class Solution:
    """
    Use DFS and calcuate max depth from each branch recursively

    Time Complexity: O(n) iterate through whole tree
    Space Complexity: O(n) the depth of the deepest branch as the DFS builds a recursion stack.
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root, depth):
            if not root:
                return depth-1
            return max( dfs(root.left, depth+1) , dfs(root.right, depth+1) )
            
        
        if root:
            ans = dfs(root, 1)
        return ans