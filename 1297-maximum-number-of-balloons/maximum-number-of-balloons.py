class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        have = {}
        need = {
            'b': 1,
            'a':1,
            'l':2,
            'o':2,
            'n':1
        }

        for c in range(0,len(text)):

            if text[c] in have:
                have[text[c]] +=1
            else:
                have[text[c]] =1
        
        res = []

        for key,values in need.items():
            temp = have.get(key,0)//values
            res.append(temp)

        
        return min(res)
        

