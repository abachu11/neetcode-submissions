from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(lambda: 0)

        # Count the frequency of each number
        for num in nums:
            res[num] += 1
        
        # Sort the items by frequency in descending order and get the top k keys
        sorted_keys = sorted(res.items(), key=lambda x: x[1], reverse=True)
        
        # Extract the keys of the top k elements
        top_k = [key for key, value in sorted_keys[:k]]
        
        return top_k
