int numWaterBottles(int numBottles, int numExchange) {
    int count = 0;
    while (numBottles>=numExchange) {
        int sets_drank = (int) (floor(numBottles/numExchange));
        count = count + sets_drank*numExchange;
        numBottles = numBottles-(sets_drank*numExchange)+sets_drank;
    } 
    return count + numBottles;
}
