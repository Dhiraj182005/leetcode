class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {
        }

        for i in s:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] = 1

        odd = False
        res = 0

        for key,values in freq.items():
            if values % 2 == 0:
                res +=values
            else:
                odd = True
        
        if odd == False:
            return res
        else:
            for key,values in freq.items():
                if values % 2 != 0:
                    res += values - 1

        
        return res +1

        