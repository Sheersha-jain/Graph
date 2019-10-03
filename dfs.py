# depth first search in graph

from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edges(self, u, v):
        self.graph[u].append(v)

    def dfs(self):
        visited = [False]*len(self.graph)
        for i in range(len(self.graph)):
            if visited[i]== False:
                self.dfsAct(i, visited)

    def dfsAct(self, vertex, visited):
        visited[vertex] =  True
        print(vertex)
        for i in self.graph[vertex]:
            if visited[i]==False:
                self.dfsAct(i, visited)
