"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    """
    Traverse in pre-order: root, left, right

    Time Complexity: O(n)
    Space Complexity: O(n) 
    """
    def preorder(self, root: 'Node') -> List[int]:
        # ========= Recursive traversal ===================
        # def pre(tree, ans):
        #     if tree == None:
        #         return ans

        #     ans.append(tree.val)
        #     for branch in tree.children:
        #         pre(branch, ans)
        #     return ans
        # ans = []
        # return pre(root, ans)

        ans = []
        if root:
            stack = [root]
            while stack:
                top = stack.pop()
                ans.append(top.val)
                for i in range(len(top.children)-1, -1, -1):
                    stack.append(top.children[i])

        return ans