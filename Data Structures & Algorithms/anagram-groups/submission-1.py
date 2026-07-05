class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## worst (m x nlogn) where m-> no of words, n-> avg len of word
        res = []
        visited = [0] * len(strs)
        for i in range(len(strs)):
            if visited[i] != 1:
                curr = strs[i]
                visited[i] = 1
                res_temp = [curr]
                for j in range(i+1,len(strs)):
                    if visited[j] != 1:
                        comp = strs[j]
                        ## anagrams when sorted are same
                        if sorted(curr) == sorted(comp):
                            ## insert to res_temp
                            visited[j] = 1
                            res_temp.append(comp)
                res.append(res_temp) 
        return res
