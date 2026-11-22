class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        arr_1 = [i**2 for i in nums if i <0]
        arr_2 = [i**2 for i in nums if i >=0]        
        if len(arr_1) == 0:
            for i in range(0,len(nums)):
                nums[i]=nums[i]**2
            
            return nums
        if len(arr_2) == 0:
            for i in range(0,len(nums)):
                nums[i]=nums[i]**2
            nums.reverse()
            return nums

        arr_1.reverse()

        final_ans = []

        i = 0
        j = 0
        # k = 0

        while(i<len(arr_1) and j<len(arr_2)):

            if arr_1[i] < arr_2[j]:
                final_ans.append(arr_1[i])
                i+=1
            elif arr_1[i] >= arr_2[j]:
                final_ans.append(arr_2[j])
                j+=1
        while i < len(arr_1):
            final_ans.append(arr_1[i])
            i+=1
        while j < len(arr_2):
            final_ans.append(arr_2[j])
            j+=1

        return final_ans


    
