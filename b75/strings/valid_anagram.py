class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for char in s:
            hashmap[char] = 1 + hashmap.get(char, 0)
        
        for char in t:
            if char in hashmap:
                hashmap[char] -= 1
                if hashmap[char] == 0:
                    del hashmap[char]
            else:
                return False
        return hashmap == {}