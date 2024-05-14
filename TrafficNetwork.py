# https://vjudge.net/problem/SPOJ-TRAFFICN
from heapq import heappush, heappop
from sys import stdin

INF = int(1e9)

t = int(input())

def Dijkstra(s, graph, dist):
    dist[s] = 0
    pq = [(0, s)]

    while pq:
        w, u = heappop(pq)

        for weight, v in graph[u]:
            if weight > dist[v]: continue
            if w + weight < dist[v]:
                dist[v] = w + weight
                heappush(pq, (dist[v], v))

for _ in range(t):
    n, m, k, s, t = map(int, stdin.readline().split())

    DistS = [INF] * (n + 1)
    DistT = [INF] * (n + 1)
    graphS = [[] for _ in range(n + 1)]
    graphT = [[] for _ in range(n + 1)]

    for _ in range(m):
        di, ci, li = map(int, stdin.readline().split())
        graphS[di].append((li, ci))
        graphT[ci].append((li, di))

    Dijkstra(s, graphS, DistS)
    Dijkstra(t, graphT, DistT)

    res = DistS[t]

    for _ in range(k):
        uj, vj, qj = map(int, stdin.readline().split())
        res = min(res, DistS[uj] + qj + DistT[vj], DistS[vj] + qj + DistT[uj])

    print(res if res!= INF else -1)


'''
1
4 5 3 1 4
1 2 13
2 3 19
3 1 25
3 4 17
4 1 18
1 3 23
2 3 5
2 4 25	
'''