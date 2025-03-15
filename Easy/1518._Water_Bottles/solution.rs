// Beats 100% Time 100% Space
impl Solution {
    pub fn num_water_bottles(mut num_bottles: i32, num_exchange: i32) -> i32 {
        let mut count:i32 = 0;
        while num_bottles >= num_exchange {
            let mut sets_drank:i32 = num_bottles / num_exchange ;
            count += sets_drank*num_exchange;
            num_bottles = num_bottles-(sets_drank*num_exchange)+sets_drank;
        }
        return count + num_bottles
    }
}
