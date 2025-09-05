from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cache = {i:[] for i in range(numCourses)}
        visit = set()
        for prerequisite in prerequisites:
            course, prereq = prerequisite
            cache[course].append(prereq)

        # every prereq has now been added to the cache... Some numbers will not be present. This means that they do not have any prereq.
        def dfs(num):
            if num in visit:
                return False
            

            if cache[num] == []:
                # there are no prereqs.
                return True
            visit.add(num)

            # there are some prereqs.
            for course in cache[num]:
                if dfs(course) == False:
                    return False
            visit.remove(num)
            cache[num] = []
            return True
        for course in range(numCourses):
            if not dfs(course): return False
        return True