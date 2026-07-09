class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i : [] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preMap[crs].append(pre)

        # visitSet to maintain and detect cycles
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            ## terminal node
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False: return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            ## to cover disconnected graphs
            if not dfs(crs):
                return False
        return True

