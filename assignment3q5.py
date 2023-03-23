from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def bfs(self, start_node):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(start_node)
        visited[start_node] = True
        
        while queue:
            node = queue.pop(0)
            print(node, end=' ')
            
            for neighbour in self.graph[node]:
                if not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour] = True
                    
    def dfs(self, start_node):
        visited = [False] * (max(self.graph) + 1)
        self._dfs_util(start_node, visited)
        
    def _dfs_util(self, node, visited):
        visited[node] = True
        print(node, end=' ')
        
        for neighbour in self.graph[node]:
            if not visited[neighbour]:
                self._dfs_util(neighbour, visited)
                
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print('BFS traversal:')
g.bfs(2)
print('\nDFS traversal:')
g.dfs(2)
