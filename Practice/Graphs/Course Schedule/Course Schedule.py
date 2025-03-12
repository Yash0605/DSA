from collections import defaultdict


class Solution(object):
    def checkPrerequisites(self, course, adjacency_list, visiting, visited):
        visiting[course] = True

        for neighbor in adjacency_list[course]:
            if not visiting[neighbor] and not visited[neighbor]:
                if not self.checkPrerequisites(
                    neighbor, adjacency_list, visiting, visited
                ):
                    return False
            elif visiting[neighbor]:
                return False

        visiting[course] = False
        visited[course] = True

        return True

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjacency_list = defaultdict(list)

        for a, b in prerequisites:
            adjacency_list[a].append(b)

        visiting, visited = [False] * numCourses, [False] * numCourses

        for course in range(numCourses):
            if not visiting[course]:
                if not self.checkPrerequisites(
                    course, adjacency_list, visiting, visited
                ):
                    return False

        return True
