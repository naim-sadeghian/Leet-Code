class Solution:
    """
    Use counter structure to count letter count and sum the number of even letters
    Only count 1 odd number, since this will be the center letter

    Time Complexity: O(n)
    Space Complexity: O(1) max dictionary size is 26*2 (caps + lowercase letters)
    """
    def longestPalindrome(self, s: str) -> int:
        #sum if even + longest odd
        count = Counter(s)
        odd = 0
        sum = 0
        for c in count.values():
            if c % 2 == 0:
                sum += c # add even numbers
            else:
                # add first odd number seen (this will be the center)
                if not(odd):
                    sum += 1
                    odd += 1
                sum += c-1 # remove 1 to make even


        return sum