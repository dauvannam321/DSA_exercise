# https://vjudge.net/problem/SPOJ-SOCIALNE

INF = float('inf')

def FloyWarshall(graph, dist, V):
    for i in range(V):
        for j in range(V):
            if i == j: dist[i][j] = 0
            elif graph[i][j] == 'Y': dist[i][j] = 1
            else: dist[i][j] = INF

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] < INF and dist[k][j] < INF:
                    dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

    # for i in dist:
    #     print(i)

T = int(input())

for _ in range(T):
    graph = []
    
    line = list(input().strip(" "))
    # print(line)
    graph.append(line)
    V = len(line)
    for _ in range(V - 1):
        graph.append(list(input().strip(" ")))

    dist = [[None] * V for _ in range(V)]
    
    FloyWarshall(graph, dist, V)

    id = 0
    Maxcount = 0
    for i in range(V):
        count = 0
        for j in range(V):
            if dist[i][j] == 2:
                count += 1

        if count > Maxcount: 
            Maxcount = count
            id = i

    print(id, Maxcount)