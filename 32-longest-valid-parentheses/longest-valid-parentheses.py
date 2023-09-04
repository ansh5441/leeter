class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Initialize variables to keep track of open and close parentheses
        open_count = 0
        close_count = 0
        string_length = len(s)
        
        # Initialize variable to store the length of the longest valid parentheses substring
        max_length = 0
        
        # Forward pass: Iterate through the string from left to right
        for i in range(string_length):
            if s[i] == "(":
                open_count += 1
            else:
                close_count += 1
            
            if open_count == close_count:
                max_length = max(max_length, open_count * 2)
            elif close_count > open_count:
                open_count, close_count = 0, 0
        
        # Reset counts for backward pass
        open_count, close_count = 0, 0
        
        # Backward pass: Iterate through the string from right to left
        for i in range(string_length - 1, -1, -1):
            if s[i] == "(":
                open_count += 1
            else:
                close_count += 1
            
            if open_count == close_count:
                max_length = max(max_length, open_count * 2)
            elif open_count > close_count:
                open_count, close_count = 0, 0
        
        return max_length
