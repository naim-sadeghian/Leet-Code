class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Iterate in reverse, since nums1 has m blank positions there should
        be no overwritting of informaction in the array.
        Time Complexity: O(N)
        Space Complexity: O(1) on same array
        """
        pointer = m + n - 1
        n = n-1
        m = m-1

        while(pointer >= 0):
            if n < 0:
                break
            elif m < 0: #remove from n becuase it is not empty
                nums1[pointer] = nums2[n]
                n = n - 1
            elif nums1[m] >= nums2[n]:
                nums1[pointer] = nums1[m]
                m = m - 1
            else:
                nums1[pointer] = nums2[n]
                n = n - 1
            pointer = pointer - 1
