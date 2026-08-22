class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        answer = 0

        for i in range(1,len(timeSeries)):
            if (timeSeries[i] - timeSeries[i-1]) < duration:
                answer +=timeSeries[i] - timeSeries[i-1]
            else:
                answer += duration

        return answer+duration 
        