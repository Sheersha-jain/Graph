from collections import defaultdict

graph = defaultdict(list)
def add_edges(graph, u, v):
    graph[u].append(v)

def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbor in graph[node]:
            edges.append((node, neighbor))
    return edges

add_edges(graph,1,2)
add_edges(graph,1,3)
add_edges(graph,4,5)
add_edges(graph,3,4)
print(generate_edges(graph))
