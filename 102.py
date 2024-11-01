class Solution:
    """
    Use BFS per level. Use queue to save all level children

    Time Complexity: O(n) iterate tree
    Space Complexity: O(n) the max size will be the last level of a full tree which is n/2
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        ans = []
        if not root:
            return []
        while(q):
            #pop all children on the level and add new children to queue
            aux = []
            for _ in range(len(q)):
                node = q.popleft()
                aux.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(aux) #Add children of that level to answer
        return ans