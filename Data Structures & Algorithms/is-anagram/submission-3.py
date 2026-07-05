class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = sorted(s)
        # t = sorted(t)
        # return s == t

        hm1 = {}
        hm2 = {}
        for char in s:
            try:
                hm1[char]+=1
            except:
                hm1[char] = 1
        for char in t:
            try:
                hm2[char]+=1
            except:
                hm2[char] = 1
        ## make sure you are checking for the one which has more
        ## length so that , if keys dont exists we return false
        if len(hm1.keys()) < len(hm2.keys()):
            hm1,hm2 = hm2,hm1
        ## now compare the counts
        for k,v in hm1.items():
            try:
                if hm2[k] == v:
                    continue
                else:
                    return False
            except:
                return False
        return True