class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1
        ans = []
        while k !=0:
            key = max(freq,key=freq.get)
            ans.append(key)
            k -=1
            del freq[key]

        return ans