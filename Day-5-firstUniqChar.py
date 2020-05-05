class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hashmap = {}
        for char_ in set(s):
            hashmap[char_] = s.count(char_)
        
        for idx in range(0,len(s)):
            if hashmap[s[idx]] == 1:
                return idx
            
        return -1
