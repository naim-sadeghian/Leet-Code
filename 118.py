class Solution:
    """
    Generate new row based on previous row values

    Time Complexity: O(n)
    Space Complexity: O(n^2) 
    """
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = [[1]]
        for depth in range(numRows-1):
            aux = [1] # new row starts with 1
            last = ans[-1]
            for i in range(0, len(last)-1):
                aux.append(last[i]+last[i+1]) # add previous value pairs
            aux.append(1) # new row ends with 1
            ans.append(aux)
        return ans

