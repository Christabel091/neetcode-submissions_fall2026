class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for chars in strs:
            counts =[0]*26
            for char in chars:
                counts[ord(char)-ord('a')] += 1
            count_tups = tuple(counts)
            if count_tups  not in results:
                results[count_tups] = [chars]
            else:
                results[count_tups].append(chars)
        return list(results.values())




        