# Beats 91% runtime, beats 55.02% memory
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        candy = {}
        count = 1
        candies_given = 0
        while True:
            for i in range(num_people):
                if i not in candy.keys():
                    candy[i] = 0 
                if candies_given+count >= candies:
                    candy[i] += (candies-candies_given)
                    arr = list(candy.values())
                    if len(arr) < num_people:
                        for i in range(num_people-len(arr)):
                            arr.append(0) 
                    return arr
                candy[i] += count
                candies_given += count
                count += 1
