# https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/monks-business-day/

INF = float('inf')

T = int(input())

def BellmanFord(s):
    dist = [INF] * N
    dist[s] = 0

    for _ in range(1, N):
        for j in range(M):
            u, v, w = graph[j]
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = w + dist[u]

    for i in range(M):
        u, v, w = graph[i]
        if dist[u] != INF and dist[u] + w < dist[v]:
            return True
        
    return False

for _ in range(T):
    N, M = map(int, input().split())

    graph = []

    for _ in range(M):
        i, j, C = map(int, input().split())
        graph.append((i - 1, j - 1, -C))

    if BellmanFord(0):
        print("Yes")
    else:
        print("No")

'''
2
5 6
1 2 2
2 3 -1
3 4 -7
4 5 0
2 3 -7
3 5 6
5 8
1 5 10
2 3 -6
5 2 5
4 5 9
1 5 1
2 4 -10
2 3 -2
4 1 1
'''