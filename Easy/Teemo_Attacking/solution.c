// Beats 100% Runtime, Beats 53.61% Memory
int findPoisonedDuration(int* timeSeries, int timeSeriesSize, int duration) {
    int ttl = 0;
    for (int i=0; i < timeSeriesSize-1; i++) {
        if (timeSeries[i] + duration - 1 < timeSeries[i+1]) {
            ttl=ttl+duration;
        }
        else {
            ttl = ttl + (timeSeries[i+1] - timeSeries[i]);
        }
    }

    return ttl + duration;
}
