# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Time Complexity: O(n) iterate tree size twice
    Space Complexity: O(n) create array of same size as tree
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        visit_order = []

        """
        fill out visit order array using dfs
        """
        def dfs(root):
            if (not root):
                return
            dfs(root.left)
            visit_order.append(root.val)
            dfs(root.right)

        dfs(root)

        #Iterate visit order and see if it is ascending
        past = float("-inf")
        for value in visit_order:
            if value <= past:
                return False
            past = value
        return True
    