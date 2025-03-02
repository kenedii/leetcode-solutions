# Beats 100% Runtime, Beats 90.33% Memory
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        items = {}
        for item in nums1:
            items[item[0]] = item[1] # Add item[0]:item[1] to items
        for item in nums2:
            if item[0] in items:
                items[item[0]] += item[1] # Add item[1] to items[item[0]]
            else:
                items[item[0]] = item[1] # Add item[0]:item[1] to items 
        arr = [[k,v] for k,v in items.items()] # Construct array of [[k,v]]
        arr.sort(key=lambda x: x[0]) # Sort by k for [[k,v]] in arr
        return arr
