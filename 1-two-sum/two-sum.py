class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_elements = {}
        
        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in check_elements:
                return [i,check_elements[sub]]
            else:
                check_elements[nums[i]] = i
        