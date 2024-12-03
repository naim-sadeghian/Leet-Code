class Solution:
    """
    Modified binary search:
    Treat the left, right and middle positions as if the matrix were flattened
      - Row is given by whole division of width
      - Column is given by modulus of width
    Time Complexity: O(n^2)
    Space Complexity: O(1) done in place
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        width = len(matrix[0])
        left = 0 
        right = (width * height) - 1

        while(left <= right):
            mid = (left+right)//2
            i = (mid // width)
            j = mid % width
            # print("Mid es: ", mid, "SSu valor es: ", matrix[i][j] )
            # print(mid, i,j)
            if(matrix[i][j] == target):
                return True
            elif(matrix[i][j] < target):
                left = mid+1
            else:
                right = mid-1
        return False
            

        