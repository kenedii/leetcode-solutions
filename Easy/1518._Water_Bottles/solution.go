// Beats 100% Time 63.64% Space
func numWaterBottles(numBottles int, numExchange int) int {
    count := 0
    for numBottles >= numExchange {
        sets_drank := numBottles/numExchange
        count=count+sets_drank*numExchange
        numBottles = numBottles-(sets_drank*numExchange)+sets_drank
    }
    return count + numBottles
}
