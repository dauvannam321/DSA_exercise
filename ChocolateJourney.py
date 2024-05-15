# https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/successful-marathon-0691ec04/

from heapq import heappush, heappop

def Dijkstra(s):
    dist = [INF] * (N + 1)
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

N, M, k, x = map(int, input().split())

graph = [[] for _ in range(N + 1)]

available = list(map(int, input().split()))

for _ in range(M):
    u, v, d = map(int, input().split())
    graph[u].append((d, v))
    graph[v].append((d, u))

A, B = map(int, input().split())

distA = Dijkstra(A)
distB = Dijkstra(B)
res = INF

for i in available:
    if distB[i] <= x:
        res = min(res, distA[i] + distB[i])

print(res if res != INF else -1)