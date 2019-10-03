graph = {'a':['c'],
         'b':['d'],
         'c':['e'],
         'd':['a', 'd'],
         'e':['b', 'c'] }
def find_all_path(graph, start, end, path= []):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_path(graph, node, end, path)
        for new_path in new_paths:
            paths.append(new_path)
    return paths

print(find_all_path(graph, 'd', 'a'))


