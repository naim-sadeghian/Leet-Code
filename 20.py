class Solution:
    """
    Use stack to check if last opening char coincides with las closing char
    Used dictionary so I didn't have to write all cases

    Time Complexity: O(n) iterate once
    Space Complexity: O(n) queue could possible grow to size of list if all chars are openers
    """
    def isValid(self, s: str) -> bool:
        closers = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        q = []
        for char in s:
            #check if it is an opener
            if char in closers:
                q.append(char)
            else:
                #Check if there are openers
                if len(q):
                    if closers[ q.pop() ] != char:
                        return False
                else:
                    return False

        #if there are still queued openers it is not valid
        return len(q) == 0 