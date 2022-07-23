impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let mut xmut = x;
        let mut y = 0;
        while xmut > 0 {
            y = y * 10 + xmut % 10;
            xmut = xmut / 10;
        }
        x == y
    }
}