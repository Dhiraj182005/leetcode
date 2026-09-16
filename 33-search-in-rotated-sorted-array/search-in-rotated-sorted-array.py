class Solution:
    def search(self, nums: list[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while high >= low:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[low]:
                if (target <= nums[mid]) and (target >= nums[low]):
                    high = mid -1
                else:
                    low = mid+1
            else:
                if (target >= nums[mid]) and (target <= nums[high]):
                    low = mid +1
                else:
                    high = mid -1 

            

        
        return -1
            
        