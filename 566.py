class Solution:
    """
    First Solution, add rows when counter reaches matrix width size

    Time Complexity: O(n^2)
    Space Complexity: O(n^2) 
    """
    # def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    #     if r * c != len(mat) * len(mat[0]):
    #         return mat
    #     ans = []
    #     rowAux = []
    #     i = 0
    #     for row in mat:
    #         for elem in row:
    #             if i == c:
    #                 ans.append(rowAux)
    #                 i = 0
    #                 rowAux = []
    #             rowAux.append(elem)
    #             i += 1
    #     ans.append(rowAux)
    #     return ans

    """
    Flatten matrix into array and build using array chunks

    Time Complexity: O(n)
    Space Complexity: O(n^2) 
    """
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat

        flat = []

        for row in mat:
            flat += row #list addition

        #append new row based on new column width
        for i in range(r):
            ans += [ flat[i*c:i*c+c] ]
        return ans