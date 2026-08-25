class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_elements = {}
        result = []

        for i in range(0,len(nums)):
            total = target - nums[i]
            if total in check_elements:
                # result.append(nums[total],i)
                return [check_elements[total],i]
            else:
                check_elements[nums[i]] = i
        return result
        