# https://vjudge.net/problem/LightOJ-1174

from heapq import heappush, heappop

def Dijkstra(s):
    dist = [INF] * N
    dist[s] = 0
    pq = [(0, s)]

    while pq:
        w, u = heappop(pq)

        if w > dist[u]: continue

        for weight, v in graph[u]:
            if w + weight < dist[v]:
                dist[v] = w + weight
                heappush(pq, (dist[v], v))

    return dist

INF = int(1e9)
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    R = int(input())

    graph = [[] for _ in range(N)]
    
    for _ in range(R):
        u, v = map(int, input().split())
        graph[u].append((1, v))
        graph[v].append((1, u))

    s, d = map(int, input().split())

    distS = Dijkstra(s)
    distD = Dijkstra(d)
    res = 0

    for i in range(N):
        res = max(res, distS[i] + distD[i])

    print("Case {}: {}".format(t, res))