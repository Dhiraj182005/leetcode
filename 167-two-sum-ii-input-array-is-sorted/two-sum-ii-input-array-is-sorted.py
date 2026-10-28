class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i =0
        j = len(numbers) - 1

        while i < j:
            add = numbers[i] + numbers[j]
            if add == target:
                return [i+1,j+1]
            elif add < target:
                i +=1
            else:
                j -=1