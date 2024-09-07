from collections import deque
from typing import Dict, Deque, List, Optional, Set


# GraphNode is used for adjacency list
class GraphNode:
    
    def __init__(self, val) -> None:
        self.val = val
        self.neighbors: List = []


# Or use a HashMap
adj_list: Dict = {}

# Given directed edges, build an adjacency list
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

for src, dst in edges:
    if src not in adj_list:
        adj_list[src] = []
    if dst not in adj_list:
        adj_list[dst] = []
    adj_list[src].append(dst)

# This will give us {'A': ['B'], 'B': ['C', 'E'], 'C': ['E'], 'E': ['D'], 'D': []}
# It means the vertex A has an edge directed to vertex B, and so on.


# Use DFS to count the number of paths that lead from a source to destination.
# Assume source is vertex A and destination is vertex E. visit is set()
def dfs(
    node: Optional[GraphNode],
    target: Optional[GraphNode],
    adj_list: Dict,
    visit: Set,
) -> int:
    
    # base cases
    if node in visit:
        return 0
    
    if node == target:
        return 1

    count = 0
    visit.add(node)
    for neighbor in adj_list[node]:
        count += dfs(neighbor, target, adj_list, visit)
    
    visit.remove(node)
    
    return count


# Use BFS to find the shortest path from node to target.
def bsf(
    node: Optional[GraphNode],
    target: Optional[GraphNode],
    adj_list: Dict,
) -> int:
    
    visit: Set = set()
    queue: Deque = deque()
    
    length = 0
    
    # starts with given node
    visit.add(node)
    queue.append(node)
    
    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()
        
            if curr == target:
                return length
        
            for neighbor in adj_list[curr]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)
        
        length += 1