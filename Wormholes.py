# https://vjudge.net/problem/UVA-558

from sys import stdin

INF = int(1e6)

t = int(stdin.readline())

def BellmanFord(graph):
    dist = [INF] * n
    dist[0] = 0

    for i in range(1, n):
        for j in range(m):
            u, v, w = graph[j]

            if dist[u] != INF and w + dist[u] < dist[v]:
                dist[v] = w + dist[u]

    for i in range(m):
        u, v, w = graph[i]
        if dist[u] != INF and w + dist[u] < dist[v]:
            return True
    
    return False

for _ in range(t):
    n, m = map(int, stdin.readline().split())

    graph = []

    for _ in range(m):
        x, y, t = map(int, stdin.readline().split())
        graph.append((x, y, t))

    if BellmanFord(graph):
        print("possible")
    else:
        print("not possible")

'''
2
3 3
0 1 1000
1 2 15
2 1 -42
4 4
0 1 10
1 2 20
2 3 30
3 0 -60
'''