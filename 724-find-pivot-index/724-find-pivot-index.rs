impl Solution {
    pub fn pivot_index(nums: Vec<i32>) -> i32 {
        let mut left_sum = 0;

            let mut left_sum = 0;

            // find sum of all numbers
            let sum: i32 = nums.iter().sum();

            for i in 0..nums.len() {
                if left_sum == sum - left_sum - nums[i] {
                    return i as i32;
                }
                left_sum += nums[i];
            }
            -1
        
        
    }
}