class Solution:
    """
    Create a set of used letters. Use 2 pointers:
        right one always moves forward
        left one stays at the begining of a word and moves forwards once a repeated letters is reached
    Move left pointer until you reach the letter that is repeated and remove all the letters in between
    Save max

    Time Complexity: O(n) iterate with 2 pointers
    Space Complexity: O(1) Set wont grow beyond accepted chars, no matter the length of s
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window = set()
        best = 0
        for right in range(len(s)):
            while(s[right] in window):
                window.remove(s[left])
                left += 1
            window.add(s[right])
            best = max(best, right-left+1)
        return best

        
            
                
            


            