class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp.keys():
                ## if we see the char in current window, 
                ## move the window start to next of previous index
                l = max(mp[s[r]] + 1, l)
            
            ## update the latest index of current element in map
            mp[s[r]] = r

            ## check max 
            res = max(res,r-l+1)
        return res

            