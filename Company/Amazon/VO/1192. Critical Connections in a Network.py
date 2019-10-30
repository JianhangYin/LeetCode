"""
This is a typical Tarjan problem.
Ideas:
1. By removing a edge, we will increase the number of the connected components.
2. If we have two lists, DFN and LOW.
    DFN is a list recording the order of DFS for each vertex.
    LOW is a list recording the lowest order of its neighbour except its parent.
3. If LOW[v] is larger than DFN[u], (u, v) is the only edge, which means that it is critical connection.
"""
from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: list) -> list:
        DFN = [-1] * n
        LOW = [-1] * n
        parent = [-1] * n
        self.time = 0
        res = []

        def Tarjan(u):
            DFN[u] = self.time
            LOW[u] = self.time
            self.time += 1
            for v in graph[u]:
                if DFN[v] == -1:
                    parent[v] = u
                    # DFS
                    Tarjan(v)
                    # Update the LOW[u]
                    LOW[u] = min(LOW[u], LOW[v])
                    if LOW[v] > DFN[u]:
                        res.append([u, v])
                # if v is explored, we still need to check and update the value of LOW[u]
                elif parent[u] != v:
                    LOW[u] = min(LOW[u], DFN[v])

        graph = defaultdict(list)
        for edge in connections:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        for i in range(n):
            if DFN[i] == -1:
                Tarjan(i)
        return res

