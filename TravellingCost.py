# https://vjudge.net/problem/SPOJ-TRVCOST

import heapq

INF = int(1e9)

N = int(input())

graph = [[] for _ in range(501)]
roads = [tuple(map(int, input().split())) for _ in range (N)]
# print(roads)

dist = [INF for _ in range(501)]

for road in roads:
    A, B, W = road
    graph[A].append((W,B))
    graph[B].append((W,A))

# print(graph)

start = int(input())

num_end = int(input())


def Dijkstra(s):
    pq = []
    heapq.heapify(pq)

    dist[s] = 0
    heapq.heappush(pq, (0, s))

    while len(pq):
        w, u = heapq.heappop(pq)
        
        for neighbour in graph[u]:
            if w + neighbour[0] < dist[neighbour[1]]:
                dist[neighbour[1]] = w + neighbour[0]
                heapq.heappush(pq, (dist[neighbour[1]], neighbour[1]))


Dijkstra(start)


for _ in range(num_end):
    end = int(input())
    if dist[end] == INF:
        print("NO PATH")
    else:
        print(dist[end])


'''
7
0 1 4
0 3 8
1 4 1
1 2 2
4 2 3
2 5 3
3 4 2
0
4
1
4
5
7
'''