// Solution 0 - Both beat 100% runtime, this one was observed to be slightly more memory efficient
int maximumCount(int* nums, int numsSize) {
    int pos = 0;
    int neg = 0;

    for (int i = 0; i<numsSize; i++) {
        if (nums[i] > 0) {
            pos++;
        } else if (nums[i] < 0) {
            neg++;
        }
    }
    if (pos > neg) {
        return pos;
    } else {
        return neg;
    }
}

// Solution 1
#define MAX(x, y) (((x) > (y)) ? (x) : (y))
int maximumCount1(int* nums, int numsSize) {
    int pos = 0;
    int neg = 0;

    for (int i = 0; i<numsSize; i++) {
        if (nums[i] > 0) {
            pos++;
        } else if (nums[i] < 0) {
            neg++;
        }
    }
    return MAX(pos, neg);
}
