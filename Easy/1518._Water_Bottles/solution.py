# Solution 1 - Initialize count to 0, count the maximum number of possible exchanges, and add the leftovers to the count
# (Completes the maximum number of exchanges possible at every iter)
# Beats 100% time, 97.81% Space, O(log(numBottles)) time
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = 0
        while numBottles>=numExchange: # If we have enough bottles to exchange
            sets_drank = numBottles//numExchange # Drink and exchange all the bottles we can. 1 'set' of bottles = numExchange bottles
            count+=sets_drank*numExchange # Add the number of bottles drank to the count
            numBottles = numBottles-(sets_drank*numExchange)+sets_drank # Update the number of bottles left to numBottles, minus the ones we drank, plus the ones we got from the exchange
        return count + numBottles # Return the count of bottles drank + numBottles (we drink the leftovers and add them to count)
