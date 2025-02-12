# Beats 89.89% Runtime
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ttl = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i] + duration - 1 < timeSeries[i+1]:
                ttl += duration
            else:
                ttl += timeSeries[i+1] - timeSeries[i]

        return ttl + duration
