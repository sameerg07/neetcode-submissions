class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## base condition:
        ## in every substring, if there are a occurences of max element
        ## and b occurences together of all other elements
        ## k >= b (sum of counts of all elements apart from max)
        ## keep increasing r until window is valid
        ## keep increasing l until window is invalid
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            ## increase l until its invalid window
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)

        return res
        