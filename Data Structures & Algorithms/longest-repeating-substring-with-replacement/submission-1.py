class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_freq = 0
        for right in range(len(s)):
            count[s[right]] = 1+count.setdefault(s[right], 0)
            highest_char = max(count.values())
            while (right-left+1) - highest_char > k:
                count[s[left]] =count[s[left]]-1
                left+=1
            max_freq = max(max_freq, right-left+1)
        return max_freq





            
        