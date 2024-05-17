# https://lightoj.com/problem/extended-traffic

from sys import stdin

INF = int(1e6)

t = int(stdin.readline())

def BellmanFord(graph, dist):
    dist[0] = 0

    for i in range(1, n):
        for j in range(m):
            u, v, w = graph[j]

            if dist[u] != INF and w + dist[u] < dist[v]:
                dist[v] = w + dist[u]

    for i in range(m):
        u, v, w = graph[i]
        if dist[u] != INF and w + dist[u] < dist[v]:
            return False
    
    return True

for i in range(1, t + 1):
    input()
    n = int(input())
    busyness = list(map(int, input().split()))

    graph = []
    dist = [INF] * n

    m = int(input())
    for _ in range(m):
        s, d = map(int, input().split())
        graph.append((s-1, d-1, (busyness[d-1] - busyness[s-1]) ** 3))

    # print(graph)

    BellmanFord(graph, dist)

    q = int(input())
    print(f"Case {i}:")
    for _ in range(q):
        q = int(input()) - 1
        if dist[q] < 3 or dist[q] == INF: print("?")
        else: print(dist[q])

    




'''
2

5
6 7 8 9 10
6
1 2
2 3
3 4
1 5
5 4
4 5
2
4
5

2
10 10
1
1 2
1
2
'''