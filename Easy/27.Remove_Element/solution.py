# Beats 100% Runtime, Beats 82.85% Memory
class Solution:
    def removeElement(self, nums, val: int) -> int:
        if nums == []:
            return 0
        i=0
        while True:
            if nums[i] == val:
                del nums[i] # or nums.pop(i) (uses more memory)
                if i == len(nums):
                    break
            else:
                if i == len(nums)-1:
                    break
                i+=1
                continue
