class Solution:
    """
    Count total A's and consecutive L's

    Time Complexity: O(n) iterate through whole list
    Space Complexity: O(1) 
    """
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0
        for i in range(len(s)):
            if s[i] == 'A':
                absent += 1
            if s[i] == 'L':
                late += 1
            else:
                late = 0
            if absent == 2 or late == 3:
                return False
            
        return True
        