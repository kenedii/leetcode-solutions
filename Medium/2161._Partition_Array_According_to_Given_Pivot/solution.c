// Beats 94.74% Memory 39.47% runtime
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* pivotArray(int* nums, int numsSize, int pivot, int* returnSize) {
    // Step 1: Count elements less than, equal to, and greater than pivot
    int lessCount = 0, equalCount = 0, greaterCount = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < pivot) {
            lessCount++;
        } else if (nums[i] == pivot) {
            equalCount++;
        } else {
            greaterCount++;
        }
    }
    
    // Step 2: Allocate the result array with exact size
    int* result = (int*)malloc(numsSize * sizeof(int));
    
    
    // Step 3: Fill the result array in order
    int index = 0;
    // Add elements less than pivot
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < pivot) {
            result[index++] = nums[i];
        }
    }
    // Add elements equal to pivot
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == pivot) {
            result[index++] = nums[i];
        }
    }
    // Add elements greater than pivot
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > pivot) {
            result[index++] = nums[i];
        }
    }
    
    *returnSize = numsSize; // Set the size of the returned array
    return result;
}
