from typing import List

# we can use dfs to find out the num of connected components
#   we create an adjacency list for bi-directional graph
#   we take a node, perform dfs on it marking visited nodes
#   at the end, we remove the nodes that were visited from the
#   adjacency list, increment num by one and perform dfs again
#   we stop when the adjacency list is empty

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(node: int) -> None:
            if node in visited: return
            visited.add(node)
            for neighbor in adjacency_list[node]:
                dfs(neighbor)
        
        # create adjacency list
        adjacency_list = {node: [] for node in range(n)}
        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)
            
        # explore graph with dfs
        count = 0
        while adjacency_list:
            # pick a node (make it efficient) and perform dfs
            node = list(adjacency_list.keys())[0]
            visited = set()
            dfs(node)
            count += 1
            
            # remove visited nodes from graph
            for node in visited:
                adjacency_list.pop(node)
        
        return count

if __name__ == "__main__":
    sol = Solution()
    tc1 = 5, [[0,1],[1,2],[3,4]]
    tc2 = 5, [[0,1],[1,2],[2,3],[3,4]]
    tc3 = 1, []
    tc4 = 5, [[0,1],[1,2],[2,3],[3,4],[4,1]]
    print(sol.countComponents(*tc1))
    print(sol.countComponents(*tc2))
    print(sol.countComponents(*tc3))
    print(sol.countComponents(*tc4))
