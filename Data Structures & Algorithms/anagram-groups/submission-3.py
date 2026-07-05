class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## O(mxn)
        ## create e1a1t1 -> 1,0,0,0,1,.....1,0,0,0,0,0,0 : ["eat","tea"]
        res_hm = {}
        for word in strs:
            countKey = [0] * 26
            for char in word:
                asci = ord(char)-97
                # inc the index by 1 for that char
                countKey[asci] += 1
            key_tuple = tuple(countKey)
            if key_tuple in res_hm.keys():
                res_hm[key_tuple].append(word)
            else:
                res_hm[key_tuple] = [word]
        
        ## create final list out of values of hashmap
        return [res_hm[key] for key in res_hm.keys()]
                
        
        ## worst (m x nlogn) where m-> no of words, n-> avg len of word
        ## keep a visited check, whenever you go through an element. Then also add it 
        ## to visited when its an anagram of some other element 
        # res = []
        # visited = [0] * len(strs)
        # for i in range(len(strs)):
        #     if visited[i] != 1:
        #         curr = strs[i]
        #         visited[i] = 1
        #         res_temp = [curr]
        #         for j in range(i+1,len(strs)):
        #             if visited[j] != 1:
        #                 comp = strs[j]
        #                 ## anagrams when sorted are same
        #                 if sorted(curr) == sorted(comp):
        #                     ## insert to res_temp
        #                     visited[j] = 1
        #                     res_temp.append(comp)
        #         res.append(res_temp) 
        # return res
