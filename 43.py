class Solution:
    """
    Multiply by factors of 10 of each digit

    Time Complexity: O(n^2)
    Space Complexity: O(1) done in place
    """
    def multiply(self, num1: str, num2: str) -> str:
        ans = [ 0 for _ in range(len(num1)+len(num2)) ]
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                val = ans[i+j+1] + (int(num1[i]) * int(num2[j]))
                ans[i+j+1] = val % 10
                ans[i+j] += val // 10
                # print(ans, j+i, j+i+1)
                
        i = 0
        while i < len(ans)-1 and ans[i] == 0:
            i += 1
        return ''.join(map(str,ans[i:]))

