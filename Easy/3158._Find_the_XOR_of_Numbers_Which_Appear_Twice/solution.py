# Beats 100% time 84.65% space
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        nums2 = {}

        for num in nums:
            nums2[num] = 1 if num not in nums2 else nums2[num]+1
        twice = []
        for k,v in nums2.items():
            if v == 2:
                twice.append(k)
        if len(twice) == 0:
            return 0
        if len(twice) == 1:
            return twice[0]
        xor = twice[0]^twice[1]
        for i in range(2,len(twice)):
            xor^=twice[i]
        return xor

        
