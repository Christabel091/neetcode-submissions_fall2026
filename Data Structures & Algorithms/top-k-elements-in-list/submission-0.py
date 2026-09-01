class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq= {}
        for num in nums:
            if num in freq:
                freq[num] = freq[num] +1
            else:
                freq[num] = 1
        buckets = [[] for _ in range(len(nums))]
        for key, value in freq.items():
            buckets[value-1].append(key)
        results = []
        for sublist in reversed(buckets):
            for num in reversed(sublist):
                if len(results) == k:
                    break
                results.append(num)
            if len(results) == k:
                break
        return results
       




