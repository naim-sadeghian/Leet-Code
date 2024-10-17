class Solution:
    """
    Iterate array in order and move pointer in substring
    return true if pointer reached the end
    Time Complexity: O(N)
    Space Complexity: O(1) on same array
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        if len(s) > len(t):
            return False
        else:
            j = 0
            for i in range(len(t)):
                if j == len(s):
                    return True
                if t[i] == s[j]:
                    j = j + 1


        return j == len(s)