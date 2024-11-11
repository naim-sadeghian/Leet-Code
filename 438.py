class Solution:
    """
    Sliding window aproach: Look at consecutive window using Count structure to see if the letters in the window make up p

    Time Complexity: O(n)
    Space Complexity: O(1) 
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        right = 0
        count = Counter(p)
        ans = []
        if len(p) > len(s):
            return ans
        i = 0

        while left < len(s) and right < len(s):
            # print(left, right)
            while left < right:
                if s[left] in count:
                    count[s[left]] += 1
                left += 1
                if s[left-1] == s[right]:
                    break
            while right < len(s):
                # print(count, left, right, ans)
                if s[right] in count:
                    if count[s[right]] > 0:
                        count[s[right]] -= 1
                        if right - left + 1 == len(p):
                            ans.append(left)
                        right += 1
                    else: #if it is a letter in p, but was already visited
                        break
                else:
                    right += 1
                    while left < right:
                        if s[left] in count:
                            count[s[left]] += 1
                        left += 1
                    break
                    
                
                

        return ans