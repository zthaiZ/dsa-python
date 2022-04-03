from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        
        for s in strs:
            letterCount = [0] * 26
            for c in s:
                letterCount[ord(c) - ord('a')] += 1
            
            hmap[tuple(letterCount)].append(s)
            
        return hmap.values()
        
