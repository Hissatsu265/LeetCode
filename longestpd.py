class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, max_length = 0, 0
        
        def expand_around_center(left: int, right: int):
            nonlocal start, max_length
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            length = right - left - 1
            if length > max_length:
                max_length = length
                start = left + 1
        
        for i in range(len(s)):
            expand_around_center(i, i)       # Odd length palindrome
            expand_around_center(i, i + 1)   # Even length palindrome
        
        return s[start:start + max_length]
