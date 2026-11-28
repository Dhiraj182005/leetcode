class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        final_list = []
        nums = sorted(nums)

        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(len(nums)-1,2,-1):
                if j <= i:
                    break
                if j < len(nums)-1 and nums[j] == nums[j+1]:
                    continue
                left = i+1
                right = j-1
                while left < right:

                    s = nums[i]+nums[j]+nums[left]+nums[right]

                    if s == target:
                        final_list.append([nums[i], nums[left], nums[right], nums[j]])

                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left-1]:
                            left += 1

                        while left < right and nums[right] == nums[right+1]:
                            right -= 1

                    elif s < target:
                        left +=1
                    else:
                        right -=1

        return final_list