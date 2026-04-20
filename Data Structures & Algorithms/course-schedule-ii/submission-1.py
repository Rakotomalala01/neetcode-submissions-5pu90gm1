class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()
        done = set()
        order = []

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in done:
                return True

            visiting.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            done.add(crs)
            order.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return order