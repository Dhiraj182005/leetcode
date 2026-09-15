class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binarySearch(low, high, findFirst):
            ans = -1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    ans = mid

                    if findFirst:
                        # Search for an earlier occurrence
                        high = mid - 1
                    else:
                        # Search for a later occurrence
                        low = mid + 1

                elif nums[mid] < target:
                    # Target is on the right
                    low = mid + 1

                else:
                    # Target is on the left
                    high = mid - 1

            return ans

        first = binarySearch(0, len(nums) - 1, True)
        last = binarySearch(0, len(nums) - 1, False)

        return [first, last]