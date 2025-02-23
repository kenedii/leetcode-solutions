# Beats 100% Runtime, Beats 83.68% Memory
from math import floor
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        arr = [(*nums1, *nums2)] # Unpacking iterables to a tuple and converting to list is much faster than nums1 + nums2
        arr.sort()                   # However, doing nums1+nums2 beats 97.29% memory
        i = len(arr)
        if i%2 == 0: # If array length is even
            return (arr[int(i/2-0.5)] + arr[int(i/2+0.5)])/2
        return arr[int(floor(i/2))]
