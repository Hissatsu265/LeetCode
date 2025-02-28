class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="": return 0
        l=0
        max=1
        for i in range(1,len(s)):
            while s[i] in s[l:i]:
                l=l+1
            if(max<i-l+1): max=i-l+1
            
        return max
