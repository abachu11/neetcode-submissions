from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for n in nums:
            frequency[n] += 1
        
        frequency_sorted = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in frequency_sorted[:k]]
