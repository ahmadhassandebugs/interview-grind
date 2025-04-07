from typing import Optional
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# connected undirected graph
# in the adjacency list, each node's value is its index
#   so we don't have to use dicts (lists should work)
# we can build the adjacency list first and then build graph
# adjacency can be built with either dfs or bfs

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        visited = {}  # we will build new graph with this
        
        def bfs(node: Optional['Node']):
            if not node: return node
            
            queue = deque([node])  # only add nodes that are not visited
            visited[node] = Node(node.val, [])
            
            while queue:
                n = queue.popleft()
                
                for neighbor in n.neighbors:
                    if neighbor not in visited:  # create new
                        visited[neighbor] = Node(neighbor.val, [])
                        queue.append(neighbor)
                    
                    visited[n].neighbors.append(visited[neighbor])
            
            return visited[node]
                
                
        def dfs(node: Optional['Node']):
            if not node: return node
            
            # return node if it has been seen before (it's neighbors are already added)
            if node in visited: return visited[node]
            
            # clone this node and add to visited
            clone_node = Node(node.val, [])
            visited[node] = clone_node  # traversing on org and need clone
            
            # clone all neighbors of node
            clone_node.neighbors = [dfs(neighbor) for neighbor in node.neighbors]
            
            return clone_node
        
        return bfs(node)

if __name__=="__main__":
    pass
