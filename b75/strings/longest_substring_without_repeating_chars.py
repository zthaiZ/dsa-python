class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seen = set()
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            max_len = max(max_len, len(seen))
        print(seen)
        return max_len