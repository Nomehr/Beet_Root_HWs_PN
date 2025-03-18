# Lesson 29
## Task 1
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        stack.append(v)

    def transpose(self):
        transposed = Graph(self.V)
        for u in self.graph:
            for v in self.graph[u]:
                transposed.add_edge(v, u)
        return transposed

    def fill_order(self):
        visited = [False] * self.V
        stack = []
        for v in range(self.V):
            if not visited[v]:
                self.dfs(v, visited, stack)
        return stack

    def scc(self):
        stack = self.fill_order()
        transposed = self.transpose()
        visited = [False] * self.V
        components = []

        while stack:
            v = stack.pop()
            if not visited[v]:
                component = []
                transposed.dfs(v, visited, component)
                components.append(component)

        return components

g = Graph(5)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(1, 0)
g.add_edge(0, 3)
g.add_edge(3, 4)

print(g.scc())

## Task 2

import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[sys.maxsize] * vertices for _ in range(vertices)]
        for i in range(vertices):
            self.graph[i][i] = 0

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight

    def dfs(self, src, dest, visited, dist):
        visited[src] = True
        for neighbor in range(self.V):
            if self.graph[src][neighbor] != sys.maxsize and not visited[neighbor]:
                new_dist = dist[src] + self.graph[src][neighbor]
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                self.dfs(neighbor, dest, visited, dist)
        visited[src] = False

    def shortest_paths(self):
        result = [[sys.maxsize] * self.V for _ in range(self.V)]
        for i in range(self.V):
            dist = [sys.maxsize] * self.V
            dist[i] = 0
            visited = [False] * self.V
            self.dfs(i, None, visited, dist)
            result[i] = dist
        return result

g = Graph(4)
g.add_edge(0, 1, 3)
g.add_edge(1, 2, 1)
g.add_edge(2, 3, 2)
g.add_edge(0, 3, 10)

print(g.shortest_paths())