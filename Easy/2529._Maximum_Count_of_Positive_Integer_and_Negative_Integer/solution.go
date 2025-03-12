// beats 100% time 83.5% space
func maximumCount(nums []int) int {
    pos, neg := 0,0

    for i := range nums {
        if nums[i] > 0 {
            pos =pos+1
        } else if nums[i] < 0 {
            neg = neg+1
        }
    }
    if neg > pos {
        return neg
    } else {
        return pos
    }
}
