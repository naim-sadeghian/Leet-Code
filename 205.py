class Solution:
    """
    Create a dictionary and check if letters appear in same order
    Encode letter of each word with order in which it forst appeared

    Time Complexity: O(N) 
    Space Complexity: O(1) dictionaries wont be longer than the set count of different characters
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return 0
        code_s = {}
        code_t = {}
        for x in range(len(s)):
            esta_s = s[x] in code_s
            esta_t = t[x] in code_t
            if esta_s != esta_t: #The letter has appeared already in one and not the other
                return 0
            elif esta_s and code_s[s[x]] != code_t[t[x]]: #the letter is in a different position
                return 0
            elif not(esta_s) and not(esta_t):
                #encode the current letter in order
                code_s[s[x]] = len(code_s)
                code_t[t[x]] = len(code_t)
        return 1
                