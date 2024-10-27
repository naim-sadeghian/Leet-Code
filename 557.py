class Solution:
    """
    The "pretty solution"
    Use pythons string reverse to reveres words

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def reverseWords(self, s: str) -> str:
        # lis = s.split(" ")
        # ans = ""
        # for i in range(len(lis)):
        #     ans += lis[i][::-1] + " "
        # return ans[0:len(ans)-1]

        #Using lists will help, since strings are immutable
        lis = s.split(" ")
        ans = []
        for i in range(len(lis)):
            ans.append( lis[i][::-1] )
        return ' '.join(result) # Pythons equivalent to string building
