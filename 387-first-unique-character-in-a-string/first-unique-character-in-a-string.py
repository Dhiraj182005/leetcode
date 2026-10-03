class Solution:
    def firstUniqChar(self, s: str) -> int:
        record = {}

        for i in range(len(s)):

            if s[i] in record:
                record[s[i]] +=1
            else:
                record[s[i]] = 1
        
        for k in range(len(s)):
            if record[s[k]] == 1:
                return k
        
        return -1
        
