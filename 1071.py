class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Check if smallest string is a substring of the largest string
        Find the GCD of the two strings by checking the length of the strings
        Check if the largest word is a concatenation of the GCD substring

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if len(str1) > len(str2):
            largest = str1
            smallest = str2
        else:
            largest = str2
            smallest = str1



        # check if smallest string it is sub string
        for i in range( len(smallest) ):
            if str1[i] != str2[i]:
                return ""

        # find GCD
        gcd = 1
        for i in range( 1, len(smallest) + 1 ):
            if (len(str1) % i == 0) and (len(str2) % i == 0):
                gcd = i
                
        # check GCD
        substring = smallest[0:gcd]
        for i in range( len(largest)//gcd  ):
            if largest[i*gcd : (i*gcd)+gcd] != substring:
                return ""

        return str1[0:gcd]

        

        