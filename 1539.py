class Solution:
    """
    Iterate by looking at consecutive pairs. Subtract the pair difference from K until k is 0 or below
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans = 1
        if k < arr[0]:
            return k

        # Remove the previous k's so if k=6 and arr = [3,....] 
        if arr[0] != 1:
            k = k - arr[0] + 1

        i = 1 # we will be looking at current and previous so start counter in 1
        while(i < len(arr) and k):
            if arr[i] - arr[i-1] != 1:
                    if (arr[i] - arr[i-1] - 1) < k:
                        k = k - (arr[i] - arr[i-1] - 1)
                    else:
                        return arr[i-1] + k
            i += 1

        if k > 0:
            return arr[-1] + k
        
        return -1