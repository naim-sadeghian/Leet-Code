# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Encode branches as strings and check if that encoding already is present in a dictionary

    Time Complexity: O(n)
    Space Complexity: O(n*m) 
    """
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hashes = defaultdict(int) # use branch encoding to see if there is an equal branch
        ans = [] # node pointing to duplicate branch
        def dfs(root):
            # return a string to show null pointer
            if not root:
                return "*"
                
            # encoding = dfs(root.left) + "|" + dfs(root.right) + "|" + str(root.val) #| separator is vital so that encoding doesn't match [1,2] to [12]
            # used string building to be more efficient, but it is not the cleanest
            encoding = []
            encoding.append( dfs(root.left) )
            encoding.append("|")
            encoding.append( dfs(root.right) )
            encoding.append("|")
            encoding.append( str(root.val) )
            encoding_string = "".join(encoding)

            if hashes[encoding_string] == 1:
                ans.append(root)
            hashes[encoding_string] += 1
            return encoding_string

        dfs(root)

        return ans