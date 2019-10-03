# adjancy list reprentation of graphs

class AdjancyNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None]*vertices

    def add_edge(self, source, destination):
        node = AdjancyNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node

        node = AdjancyNode(source)
        node.next = self.graph[destination]
        self.graph[destination] = node

    def print_graph(self):
        for i in range(self.V):
            print("Adjancy list of vertex {} \n ",format(i), end="")
            temp = self.graph[i]
            while temp:
                print("-> {}".format(temp.vertex), end="")
                temp = temp.next
            print("\n")

if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
