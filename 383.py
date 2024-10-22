class Solution:
    """
    Use Counter collection to compare letter count in each string

    Time Complexity: O(n)
    Space Complexity: O(1) max size wont go beyond 26 lowercase english chars
    """
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        r = Counter(ransomNote)
        m = Counter(magazine)
        for (letter, count) in r.items():
            if not(letter in m) or m[letter] < count:
                return False
        return True