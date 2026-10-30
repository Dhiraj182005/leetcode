class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        k = 1

        while j <= len(nums) - 1:
            if nums[j] != nums[j-1]:
                nums[i+1] = nums[j]
                i+=1
                k+=1
            j +=1
        
        return k

            

        