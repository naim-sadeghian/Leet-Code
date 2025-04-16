class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Use python list to split the string and filter out empty strings
        Then reverse the list and join it back to a string

        Time Complexity: O(n)
        Space Complexity: O(n) create an array of size n
        """
        words = s.strip().split(" ")
        # print(words)
        words = list(filter(lambda x: x != "", words))
        return " ".join(words[::-1])

        # one liner
        # return " ".join( list(filter(lambda x: x != "", s.strip().split(" ")))[::-1] )