from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        minHeap = []
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
        for num, frequency in freq.items():
            heappush(minHeap, (num, frequency))
            if len(minHeap) > k:
                heappop(minHeap)
                
        topNumbers = []
        while minHeap:
            topNumbers.append(heappop(minHeap)[0])
            
        return topNumbers