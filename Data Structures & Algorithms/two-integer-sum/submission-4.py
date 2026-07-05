class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ##hashmap storing number->index
        hm = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in hm.keys():
                return [hm[rem],i] ##since hm[rem] is to left of i
            hm[nums[i]] = i

        # brute force
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        ## if sorted
        # i = 0
        # j = len(nums) - 1

        # while(i<j):
        #     sum1 = nums[i] + nums[j]
        #     print(nums[i],nums[j])
        #     if sum1 == target:
        #         return [i,j]
        #     elif sum1 < target:
        #         i+=1
        #     else:
        #         j-=1
