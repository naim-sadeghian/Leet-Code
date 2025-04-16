class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        First word letter awlays first, then second word letter

        Time Complexity: O(n)
        Space Complexity: O(n) create an array of size n
        """
        n = max(len(word1), len(word2))
        ans = []
        for i in range(n):
            if i < len(word1):
                ans.append(word1[i])
            if i < len(word2):
                ans.append(word2[i])
        return "".join(ans)
