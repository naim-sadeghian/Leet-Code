class Solution:
    """
    I tried linear solution to be more memory efficient 

    Time Complexity: O(n)
    Space Complexity: O(1) done in place
    """
    def compress(self, chars: List[str]) -> int:
        left, right, count = 0, 0, 1
        last = ""
        while right < len(chars):
            
            #count repeated
            while right < len(chars) and chars[right] == last:
                print(right)
                count += 1
                right += 1
            
            #add digits
            if count > 1:
                for digit in str(count):
                    chars[left] = digit
                    left += 1
            
            if right < len(chars):
                last = chars[right]
                chars[left] = chars[right]

            right += 1
            count = 1
            left += 1

        return left if right <= len(chars) else left-1