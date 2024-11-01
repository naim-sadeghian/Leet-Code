# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    DFS and record lrft -> current -> right

    Time Complexity: O(n)
    Space Complexity: O(1) 
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node):
            if not node:
                return
            
            dfs( node.left )
            ans.append( node.val )
            dfs( node.right )

        dfs( root )    
        return ans