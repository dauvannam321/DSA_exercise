# https://vjudge.net/problem/SPOJ-MICEMAZE
# https://www.spoj.com/problems/MICEMAZE/#:~:text=A%20set%20of%20laboratory%20mice%20is%20being%20trained,go%20one-way%2C%20but%20not%20the%20other%20way%20round.

import heapq

INF = int(1e9)

N = int(input())
E = int(input())
T = int(input())
M = int(input())

graph = [[] for  _ in range(N + 1)]
dist = [INF for _ in range(N + 1)]

for _ in range(M):
    a, b, t = list(map(int, input().split()))
    graph[b].append((t, a))


def Dijkstra(s):
    pq = []
    heapq.heapify(pq)

    dist[s] = 0
    heapq.heappush(pq, (0, s))

    while len(pq):
        w, u = heapq.heappop(pq) 

        for neighbor in graph[u]:
            if w + neighbor[0] < dist[neighbor[1]]:
                dist[neighbor[1]] = w + neighbor[0]
                heapq.heappush(pq, (dist[neighbor[1]], neighbor[1]))

Dijkstra(E)

count = 0
for i in range(1, N + 1):
    if dist[i] <= T:
        count += 1
# print(dist)
print(count)



'''
4 
2 
1
8
1 2 1
1 3 1
2 1 1
2 4 1
3 1 1
3 4 1
4 2 1
4 3 1
'''