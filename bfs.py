# BFS in graph

from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph =  defaultdict(list)

    def add_edges(self, u, v):
        self.graph[u].append(v)

    def bfs(self, vertex):
        visited = [False]*len(self.graph)
        queue = []
        queue.append(vertex)
        visited[vertex] = True
        while queue:
            vertex = queue.pop(0)
            print(vertex, end="")
            for i in self.graph[vertex]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]= True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.BFS(2)

