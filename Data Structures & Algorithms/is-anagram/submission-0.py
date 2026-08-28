class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dicts = {}
        dicts2 ={}
        for char in range(len(s)):
            val = dicts.setdefault(s[char], 0)
            dicts[s[char]]=1+val

            val2 = dicts2.setdefault(t[char], 0)
            dicts2[t[char]]=1+val2
        return dicts == dicts2
            


        