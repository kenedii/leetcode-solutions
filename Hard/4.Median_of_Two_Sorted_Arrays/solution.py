# Beats 100% Runtime, Beats 83.68% Memory
from math import floor
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        arr = list((*nums1, *nums2)) # Unpacking iterables to a tuple and converting to list is much faster than nums1 + nums2
        arr.sort()
        i = len(arr)
        if i%2 == 0:
            return (arr[int(i/2-0.5)] + arr[int(i/2+0.5)])/2
        return arr[int(floor(i/2))]
