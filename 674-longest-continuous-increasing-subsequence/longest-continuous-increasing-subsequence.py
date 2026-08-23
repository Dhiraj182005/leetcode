class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        previous_sequence = 1
        sequence = 1

        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                sequence +=1
            else:
                if sequence > previous_sequence:
                    previous_sequence = sequence
                sequence = 1
            
        return max(sequence,previous_sequence)
        