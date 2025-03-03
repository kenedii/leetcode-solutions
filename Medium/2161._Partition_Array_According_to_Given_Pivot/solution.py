# Beats 72.46% runtime O(n)
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, right = [], []
        pivot_count = 0
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            elif num == pivot:
                pivot_count+=1
        for i in range(pivot_count):
            left.append(pivot)
        return left + right
