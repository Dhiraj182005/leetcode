class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # freq = {}

        # for i in range(len(s)):
        #     freq[i] = i

        # for j in range(len(t)):

        #     if t[j] not in freq:
        #         return False
        

        # return True

        if len(s) != len(t):
            return False
        else:
            s= "".join(sorted(s))
            t= "".join(sorted(t))

            p1 = 0
            p2 = 0

            while p1 < len(s):
                if s[p1] != t[p2]:
                    return False
                
                p1+=1
                p2 +=1
            
        
        return True