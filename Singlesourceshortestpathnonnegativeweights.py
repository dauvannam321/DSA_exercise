# https://vjudge.net/problem/Kattis-shortestpath1
from heapq import heappop, heappush
from sys import stdin

INF = int(1e9)

def dijkstra(s):
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        w, u = heappop(pq)
        if w > dist[u]:
            continue
        for v, weight in graph[u]:
            distance = w + weight
            if distance < dist[v]:
                dist[v] = distance
                heappush(pq, (distance, v))

while True:
    n, m, q, s = map(int, stdin.readline().split())
    if n == 0 and m == 0 and q == 0 and s == 0:
        break
    
    graph = [[] for _ in range(n)]
    dist = [INF] * n
    for _ in range(m):
        u, v, w = map(int, stdin.readline().split())
        graph[u].append((v, w))
    
    dijkstra(s)
    
    for _ in range(q):
        query = int(stdin.readline())
        if dist[query] == INF:
            print("Impossible")
        else:
            print(dist[query])
    print()


'''
4 3 4 0
0 1 2
1 2 2
3 0 2
0
1
2
3
2 1 1 0
0 1 100
1
0 0 0 0
'''