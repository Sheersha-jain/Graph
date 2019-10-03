graph ={
    'a':['c'],
    'b':['d'],
    'c':['e'],
    'd':['a', 'd'],
    'e':['b', 'c']
}

def shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    shortest = None
    for node in graph[start]:
        if node not in path:
            new_path = shortest_path(graph, node, end, path)
            if new_path:
                if new_path is not shortest or len(new_path)< len(shortest):
                    shortest = new_path
    return shortest

print(shortest_path(graph, 'a', 'c'))

