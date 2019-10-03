# topological sort

from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        visited = [False]*self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalUser(i, visited, stack)
        print(stack)

    def topologicalUser(self,v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalUser(i, visited, stack)
        stack.insert(0, v)

ghelp = Graph(6)
ghelp.add_edge(5, 2);
ghelp.add_edge(5, 0);
ghelp.add_edge(4, 0);
ghelp.add_edge(4, 1);
ghelp.add_edge(2, 3);
ghelp.add_edge(3, 1);
ghelp.topological_sort()

