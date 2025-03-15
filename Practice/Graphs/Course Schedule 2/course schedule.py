from collections import defaultdict

"""
The problem reduces to find a topological sort order of the courses, which would be a DAG if it has a valid order
Since it is likely to be sparse,we use adjacency list graph data structure.
"""


class Solution:
    def visitCourses(self, course, courseGraph, visiting, visited, finalOrdering):
        visiting[course] = True

        for neighbor in courseGraph[course]:
            if visiting[neighbor]:
                return False
            elif not visited[neighbor]:
                if not self.visitCourses(
                    neighbor, courseGraph, visiting, visited, finalOrdering
                ):
                    return False

        visiting[course] = False
        visited[course] = True
        finalOrdering.append(course)

        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseGraph = defaultdict(list)
        finalOrdering = []

        for courseA, courseB in prerequisites:
            courseGraph[courseA].append(courseB)

        visiting = [False] * numCourses
        visited = [False] * numCourses

        for course in range(numCourses):
            if not visited[course]:
                if not self.visitCourses(
                    course, courseGraph, visiting, visited, finalOrdering
                ):
                    # if there is a cycle
                    return []

        # finalOrdering.reverse()

        return finalOrdering
