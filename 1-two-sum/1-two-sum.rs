use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map = HashMap::new();
        for i in 0..nums.len() {
            if map.contains_key(&(target-nums[i])) {
                return vec![map[&(target - nums[i])] as i32, i as i32];
            }
            map.insert(nums[i], i);
        }
        vec![]
        
    }
    
}
