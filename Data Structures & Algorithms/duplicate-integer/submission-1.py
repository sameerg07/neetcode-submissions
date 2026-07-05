class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for num in nums:
            try:
                hm[num]+=1
                return True
            except:
                hm[num] = 1
        return False
        