from collections import deque

# BFS Iterative
# explore all children first, before exploring their children (FIFO)
def bfs_iterative(graph, start):
    """
    Perform BFS iteratively on a graph with cycles.
    :param graph: dict, adjacency list representation of the graph
    :param start: starting node
    :return: list of nodes in BFS order
    """
    fifo = deque([start])
    visited = {start}
    bfs_list = []
    
    if start not in graph: return []
    
    while fifo:
        node = fifo.popleft()
        bfs_list.append(node)    
        for n in graph.get(node, []):
            if n not in visited:
                fifo.append(n)
                visited.add(n)
    
    return bfs_list

# BFS Recursive
def bfs_recursive(graph, queue, visited, result):
    """
    Perform BFS recursively on a graph with cycles.
    :param graph: dict, adjacency list representation of the graph
    :param queue: deque, queue of nodes to visit
    :param visited: set, visited nodes
    :param result: list, nodes in BFS order
    """
    if not queue: return result  # if nothing more to visit
    
    node = queue.popleft()
    result.append(node)
    for n in graph.get(node, []):
        if n not in visited:
            queue.append(n)
            visited.add(n)
    return bfs_recursive(graph, queue, visited, result)
    

# DFS Iterative
def dfs_iterative(graph, start):
    """
    Perform DFS iteratively on a graph with cycles.
    :param graph: dict, adjacency list representation of the graph
    :param start: starting node
    :return: list of nodes in DFS order
    """
    if start not in graph: return []
    
    lifo = deque([start])
    visited = {start}
    result = []
    
    while lifo:
        node = lifo.pop()
        result.append(node)
        for n in graph.get(node, []):
            if n not in visited:
                lifo.append(n)
                visited.add(n)
    return result

# DFS Recursive
def dfs_recursive(graph, node, visited, result):
    """
    Perform DFS recursively on a graph with cycles.
    :param graph: dict, adjacency list representation of the graph
    :param node: current node
    :param visited: set, visited nodes
    :param result: list, nodes in DFS order
    """
    if node not in graph or node in visited: return result
    
    visited.add(node)
    result.append(node)
    
    for n in graph.get(node, []):
        if n not in visited: dfs_recursive(graph, n, visited, result)

# Topological Sort
def topological_sort(graph):
    """
    Perform topological sort on a directed acyclic graph (DAG).
    :param graph: dict, adjacency list representation of the graph
    :return: list of nodes in topological order
    """
    result = []
    visited = set()    
    def dfs_post(node):
        visited.add(node)
        for n in graph.get(node, []):
            if n not in visited: dfs_post(n)
        result.append(node)
    
    for node in list(graph.keys()):
        if node not in visited: dfs_post(node)
    
    return result[::-1]

# Detect Cycle (using DFS)
def detect_cycle(graph):
    """
    Detect if there is a cycle in a directed graph.
    :param graph: dict, adjacency list representation of the graph
    :return: bool, True if a cycle exists, False otherwise
    """
    visited = set()
    call_stack = set()
    def dfs(node):
        visited.add(node)
        call_stack.add(node)
        
        for n in graph.get(node, []):
            if n not in visited:
                if dfs(n): return True
            elif n in call_stack: return True
        
        call_stack.remove(node)
        return False
    
    for node in list(graph.keys()):
        if node not in visited:
            if dfs(node): return True
    return False

# Dijkstra's Algorithm
def dijkstra(graph, start):
    """
    Find the shortest path in a graph using Dijkstra's algorithm.
    :param graph: dict, adjacency list with weights {node: [(neighbor, weight), ...]}
    :param start: starting node
    :return: dict of shortest distances from start to each node
    """
    if start not in graph: return {}
    import heapq
    # step 1. create distance list and prioirty list
    distances = {node: float('inf') for node in graph.keys()}
    distances[start] = 0
    heap = [(start, 0)]  # node, distance
    
    # step 2. greedy updates
    while heap:
        node, cur_dist = heapq.heappop(heap)
        if cur_dist > distances[node]: continue  # skip if old entry
        for neighbor, weight in graph.get(node, []):
            new_dist = cur_dist + weight
            if new_dist < distances[neighbor]:  # found shorter path
                distances[neighbor] = new_dist
                heap.append((neighbor, new_dist))
    
    return distances
                

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
    result = bfs_recursive(graph, deque(['A']), set('A'), [])
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
    # DAG
    graph_dag = {
        'A': ['C'],
        'B': ['C', 'D'],
        'C': ['E'],
        'D': ['F'],
        'E': ['F'],
        'F': []
    }
    result_dag = topological_sort(graph_dag)
    # Basic validation (more robust checks needed for guarantees)
    valid_dag = True
    if result_dag: # Check if not empty (cycle detection might return empty)
        pos = {node: i for i, node in enumerate(result_dag)}
        for node, neighbors in graph_dag.items():
            for neighbor in neighbors:
                if pos[node] > pos[neighbor]:
                    valid_dag = False; break
            if not valid_dag: break
    else:
        valid_dag = False # Empty result means cycle or error
    print("Topological Sort (DAG):", "PASS" if valid_dag and len(result_dag) == len(graph_dag) else "FAIL", result_dag)

    # Graph with cycle
    graph_cycle = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }
    result_cycle = topological_sort(graph_cycle)
    # Expect empty list or similar indication of cycle
    print("Topological Sort (Cycle):", "PASS" if not result_cycle else "FAIL", result_cycle)

def test_detect_cycle():
    # Graph without cycle (DAG)
    graph_dag = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    result_dag = detect_cycle(graph_dag)
    print("Detect Cycle (DAG):", "PASS" if not result_dag else "FAIL", result_dag)

    # Graph with cycle
    graph_cycle = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A'] # Cycle C -> A
    }
    result_cycle = detect_cycle(graph_cycle)
    print("Detect Cycle (Cycle):", "PASS" if result_cycle else "FAIL", result_cycle)

    # Graph with cycle 2
    graph_cycle_2 = {
        'A': ['B'],
        'B': ['C'],
        'C': ['D'],
        'D': ['B'] # Cycle D -> B
    }
    result_cycle_2 = detect_cycle(graph_cycle_2)
    print("Detect Cycle (Cycle 2):", "PASS" if result_cycle_2 else "FAIL", result_cycle_2)

    # Disconnected graph without cycle
    graph_disconnected_no_cycle = {
        'A': ['B'], 'B': [],
        'C': ['D'], 'D': []
    }
    result_disconnected_no_cycle = detect_cycle(graph_disconnected_no_cycle)
    print("Detect Cycle (Disconnected No Cycle):", "PASS" if not result_disconnected_no_cycle else "FAIL", result_disconnected_no_cycle)

    # Disconnected graph with cycle
    graph_disconnected_cycle = {
        'A': ['B'], 'B': [],
        'C': ['D'], 'D': ['E'], 'E': ['C'] # Cycle C->D->E->C
    }
    result_disconnected_cycle = detect_cycle(graph_disconnected_cycle)
    print("Detect Cycle (Disconnected Cycle):", "PASS" if result_disconnected_cycle else "FAIL", result_disconnected_cycle)


def test_dijkstra():
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('D', 2), ('E', 5)],
        'C': [('A', 4), ('F', 3)],
        'D': [('B', 2)],
        'E': [('B', 5), ('F', 1)],
        'F': [('C', 3), ('E', 1)],
        # Add node G reachable only via F
        # 'F': [('C', 3), ('E', 1), ('G', 2)],
        # 'G': [] # Node G
    }
    # Add G to graph for testing unreachable/further nodes
    graph['F'].append(('G', 2))
    graph['G'] = []

    result = dijkstra(graph, 'A')
    # Expected distances including G
    expected = {'A': 0, 'B': 1, 'C': 4, 'D': 3, 'E': 6, 'F': 7, 'G': 9}
    print("Dijkstra:", "PASS" if result == expected else "FAIL", result)

    # Test with a node that has no outgoing edges listed but is reachable
    graph_simple = {
        'X': [('Y', 5)],
        'Y': [] # Y has no outgoing edges listed
    }
    result_simple = dijkstra(graph_simple, 'X')
    expected_simple = {'X': 0, 'Y': 5}
    print("Dijkstra (Simple):", "PASS" if result_simple == expected_simple else "FAIL", result_simple)

    # Test with start node not in graph
    result_not_found = dijkstra(graph, 'Z')
    expected_not_found = {}
    print("Dijkstra (Start Not Found):", "PASS" if result_not_found == expected_not_found else "FAIL", result_not_found)

if __name__ == "__main__":
    test_bfs_iterative()
    test_bfs_recursive()
    test_dfs_iterative()
    # Correct the call for dfs_recursive test
    graph_dfs_rec = { 'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E'] }
    result_dfs_rec = []
    visited_dfs_rec = set()
    # Need to handle the initial call correctly if start node might not be in graph
    if 'A' in graph_dfs_rec:
        dfs_recursive(graph_dfs_rec, 'A', visited_dfs_rec, result_dfs_rec)
    expected_dfs_rec = ['A', 'B', 'D', 'E', 'F', 'C'] # Or other valid DFS orders
    # Note: DFS order depends on neighbor iteration order. This test might be brittle.
    # A better test would check properties of DFS, not exact sequence.
    print("DFS Recursive:", "PASS" if result_dfs_rec == expected_dfs_rec else "FAIL", result_dfs_rec)

    test_topological_sort()
    test_detect_cycle() # Add call to the new test
    test_dijkstra()
