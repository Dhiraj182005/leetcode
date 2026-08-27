class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        neg = 1
        pos = 0

        ans = [0]* len(nums)

        for num in nums:

            if num < 0:
                ans[neg] = num
                neg +=2
            else:
                ans[pos] = num
                pos +=2
        
        return ans
        
        