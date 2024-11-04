class Solution:
    """
    Tabulation: save the minimum amount of steps to turn string1 into string2 with a matrix of n*m 
    Where we save the minimum amount of steps to transform a string at a given position.
    Select minimum between:
    - Inserting
    - Delting
    - CHanging letter
    
    Time Complexity: O(n*m)
    Space Complexity: O(n*m) 
    """
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        memo = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    memo[i][j] = j
                elif j == 0:
                    memo[i][j] = i
                else:
                    if word1[i-1] == word2[j-1]:
                        memo[i][j] = memo[i-1][j-1] #no change
                    else:
                        memo[i][j] = min(memo[i-1][j-1], memo[i][j-1], memo[i-1][j]) + 1
        return memo[m][n]
