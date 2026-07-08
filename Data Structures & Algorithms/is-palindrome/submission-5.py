class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s)-1
        while (i<j):
            if (not(self.isAlNum(s[i]))):
                i+=1
                continue
            if (not(self.isAlNum(s[j]))):
                j-=1
                continue
            if(s[i].lower() != s[j].lower()):
                # print(s[i],s[j])
                return False
            i+=1
            j-=1
        return True
    def isAlNum(self,c):
        ordi = ord(c)
        if ordi in range(97,123) or ordi in range(65,91) or ordi in range(48,58):
            return True
        return False