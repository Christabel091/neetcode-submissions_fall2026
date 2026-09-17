class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0
        chars = {}
        left = 0
        max_val =0
        while right < len(s):
            if s[right] in chars:
                if chars[s[right]] >= left:
                    left = chars[s[right]]+1
            chars[s[right]] = right
            right+=1
            max_val = max(max_val, (right-left))
        return max_val
            


        