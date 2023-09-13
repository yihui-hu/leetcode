"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        perform DFS and recursively build out cloned graph
        """

        if not node:
          return None

        visited = {}
        def dfs(node):
          # return existing node, don't make new copy of it
          if node in visited:
            return visited[node]
          
          # making copy of node
          copy = Node(node.val)
          visited[node] = copy

          # make copies of neighbor
          for n in node.neighbors:
            new_neighbor = dfs(n)
            copy.neighbors.append(new_neighbor)
          return copy
        
        return dfs(node)
