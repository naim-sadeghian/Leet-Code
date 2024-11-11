class Solution:
    """
    Save visited numbers to make sure we are not looping infinitely

    Time Complexity: O(n)
    Space Complexity: O(n) 
    """
    def isHappy(self, n: int) -> bool:
        visited = {}
        while(not(n in visited)):

            if n == 1:
                return True

            visited[n] = True
            digits = str(n)
            n = 0
            for digit in digits:
                n += int(digit) ** 2
                # print(digit, end="")
            # print()
            