class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        result = 0
        max_diff = float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums) - 1

            while left < right:
                sum_total = nums[i] + nums[left] + nums[right]

                diff = abs(target - sum_total)

                if diff < max_diff:
                    max_diff = diff
                    result = sum_total
                
                if sum_total == target:
                    result = sum_total
                    return result
                elif sum_total > target:
                    right -=1
                else:
                    left +=1
        
        return result

