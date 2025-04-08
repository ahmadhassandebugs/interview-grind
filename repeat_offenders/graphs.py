from collections import deque

# BFS Iterative
def bfs_iterative(graph, start):
    """
    Perform BFS iteratively on a graph with cycles.
    :param graph: dict, adjacency list representation of the graph
    :param start: starting node
    :return: list of nodes in BFS order
    """
    pass  # TODO: Implement this function

# BFS Recursive
def bfs_recursive(graph, queue, visited, result):
    """
    Perform BFS recursively on a graph with cycles.
    :param graph: dict, adjacency list representation of the graph
    :param queue: deque, queue of nodes to visit
    :param visited: set, visited nodes
    :param result: list, nodes in BFS order
    """
    pass  # TODO: Implement this function

# DFS Iterative
def dfs_iterative(graph, start):
    """
    Perform DFS iteratively on a graph with cycles.
    :param graph: dict, adjacency list representation of the graph
    :param start: starting node
    :return: list of nodes in DFS order
    """
    pass  # TODO: Implement this function

# DFS Recursive
def dfs_recursive(graph, node, visited, result):
    """
    Perform DFS recursively on a graph with cycles.
    :param graph: dict, adjacency list representation of the graph
    :param node: current node
    :param visited: set, visited nodes
    :param result: list, nodes in DFS order
    """
    pass  # TODO: Implement this function

# Topological Sort
def topological_sort(graph):
    """
    Perform topological sort on a directed acyclic graph (DAG).
    :param graph: dict, adjacency list representation of the graph
    :return: list of nodes in topological order
    """
    pass  # TODO: Implement this function

# Dijkstra's Algorithm
def dijkstra(graph, start):
    """
    Find the shortest path in a graph using Dijkstra's algorithm.
    :param graph: dict, adjacency list with weights {node: [(neighbor, weight), ...]}
    :param start: starting node
    :return: dict of shortest distances from start to each node
    """
    pass  # TODO: Implement this function

################ TESTING ####################

def test_bfs_iterative():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    result = bfs_iterative(graph, 'A')
    expected = ['A', 'B', 'C', 'D', 'E', 'F']
    print("BFS Iterative:", "PASS" if result == expected else "FAIL", result)

def test_bfs_recursive():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    result = bfs_recursive(graph, deque(['A']), set(), [])
    expected = ['A', 'B', 'C', 'D', 'E', 'F']
    print("BFS Recursive:", "PASS" if result == expected else "FAIL", result)

def test_dfs_iterative():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    result = dfs_iterative(graph, 'A')
    expected = ['A', 'C', 'F', 'E', 'B', 'D']
    print("DFS Iterative:", "PASS" if result == expected else "FAIL", result)

def test_dfs_recursive():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    result = []
    dfs_recursive(graph, 'A', set(), result)
    expected = ['A', 'B', 'D', 'E', 'F', 'C']
    print("DFS Recursive:", "PASS" if result == expected else "FAIL", result)

def test_topological_sort():
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    result = topological_sort(graph)
    expected = ['A', 'C', 'B', 'D']
    print("Topological Sort:", "PASS" if result == expected else "FAIL", result)

def test_dijkstra():
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('D', 2), ('E', 5)],
        'C': [('A', 4), ('F', 3)],
        'D': [('B', 2)],
        'E': [('B', 5), ('F', 1)],
        'F': [('C', 3), ('E', 1)]
    }
    result = dijkstra(graph, 'A')
    expected = {'A': 0, 'B': 1, 'C': 4, 'D': 3, 'E': 6, 'F': 7}
    print("Dijkstra:", "PASS" if result == expected else "FAIL", result)

if __name__ == "__main__":
    test_bfs_iterative()
    test_bfs_recursive()
    test_dfs_iterative()
    test_dfs_recursive()
    test_topological_sort()
    test_dijkstra()
