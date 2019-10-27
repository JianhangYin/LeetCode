from collections import defaultdict


class Graph:
    def __init__(self, num_vertex):
        self.graph = defaultdict(list)
        self.num_vertex = num_vertex

    def add_edge(self, v, u):
        self.graph[v].append(u)

    def topological_sort_helper(self, v, visited, stack):
        visited[v] = True
        for u in self.graph[v]:
            if not visited[u]:
                self.topological_sort_helper(u, visited, stack)
        stack.insert(0, v)

    def topological_sort(self):
        visited = [False] * self.num_vertex
        stack = []
        for i in range(self.num_vertex):
            if not visited[i]:
                self.topological_sort_helper(i, visited, stack)
        print(stack)


g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.topological_sort()

