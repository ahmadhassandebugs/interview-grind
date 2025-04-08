from typing import List, Dict

# this is about detecting cycles in a graph
# we can use dfs to check if there's any cycle
#   if in the dfs call stack we see a node that
#   has been visited before, it's a cycle and we
#   return True immediately.
#   Otherwise, we keep exploring the graph
# we will need to maintain a list of ancestors at
#   any point. instead of using a growing list, we
#   can use a boolean dict (search will be O(1))
# in dfs, we need to know the neighbors of a node
#   we are visiting. we can build an adjacency list first.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def dfs(node, ancestors) -> bool:  # true if cycle detected
            # check for cycle
            if ancestors[node]: return True  # in dfs callstack
            
            # check if visited before
            if node in visited: return False  # visited but no cycle
            
            # add to the dfs callstack
            ancestors[node] = True
            
            # mark as visited
            visited.add(node)
            
            # call dfs on all neighbors to detect cycles
            for neighbor in adjacency_list[node]:
                if dfs(neighbor, ancestors):
                    return True  # return true immediately
            
            # remove from the dfs callstack after exploring
            ancestors[node] = False
            
            return False
        
        # build adjacency list
        adjacency_list = {node: [] for node in range(numCourses)}
        for course, prereq in prerequisites:
            adjacency_list[prereq].append(course)
        
        # detect cycle using dfs
        ancestors = {node: False for node in range(numCourses)}
        visited = set()
        
        for node in range(numCourses):  # run over all (can be disconnected)
            if dfs(node, ancestors):
                return False
        
        return True

if __name__=="__main__":
    sol = Solution()
    tc1 = 2, [[1,0]]
    tc2 = 2, [[1,0],[0,1]]
    tc3 = 3, [[1,2],[0,2]]
    tc4 = 3, [[1,2],[0,2],[2,1]]
    tc5 = 1, []
    print(sol.canFinish(*tc1))
    print(sol.canFinish(*tc2))
    print(sol.canFinish(*tc3))
    print(sol.canFinish(*tc4))
    print(sol.canFinish(*tc5))
    