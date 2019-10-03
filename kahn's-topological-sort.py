# Kahn's algorithm for topological sorting

from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        indegree = [0]*(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                indegree[j]+= 1

        queue = []
        for i in range(self.V):
            if indegree[i] == 0:
                queue.append(i)

        visited = 0
        topological_result = []
        while queue:
            u = queue.pop(0)
            topological_result.append(u)
            for i in self.graph[u]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
            visited+=1
        if visited != self.V:
            print("topological sort not possible, cycle exists")
        else:
            print(topological_result)