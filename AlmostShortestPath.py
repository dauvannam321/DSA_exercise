# https://vjudge.net/problem/SPOJ-SAMER08A

from heapq import heappush, heappop

INF = int(1e9)

def Dijkstra(s, graph, dist):
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
    

while True:
    N, M = map(int, input().split())
    if N == M == 0: break

    S, D = map(int, input().split())

    graph = [[] for _ in range(N)]
    graphS = [[] for _ in range(N)]
    graphD = [[] for _ in range(N)]

    dist = [INF] * N
    distS = [INF] * N
    distD = [INF] * N

    for _ in range(M):
        u, v, p = map(int ,input().split())
        graphS[u].append((p, v))
        graphD[v].append((p, u))

    Dijkstra(S, graphS, distS)
    Dijkstra(D, graphD, distD)
    shortest_path = distS[D]
    for u in range(N):
        for w, v in graphS[u]:
            if distS[u] + w + distD[v] != shortest_path:
                graph[u].append((w, v))

    Dijkstra(S, graph, dist)
    print(dist[D] if dist[D] != INF else -1)

# C++
# #include <iostream>
# #include <vector>
# #include <queue>
# #include <limits>
# #include <tuple>

# using namespace std;

# const int INF = 1e9;

# void Dijkstra(int s, const vector<vector<pair<int, int>>>& graph, vector<int>& dist) {
#     dist[s] = 0;
#     priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
#     pq.push({0, s});

#     while (!pq.empty()) {
#         int w = pq.top().first;
#         int u = pq.top().second;
#         pq.pop();

#         if (w > dist[u]) continue;
#         for (const auto& edge : graph[u]) {
#             int weight = edge.first;
#             int v = edge.second;
#             if (w + weight < dist[v]) {
#                 dist[v] = w + weight;
#                 pq.push({dist[v], v});
#             }
#         }
#     }
# }

# int main() {
#     while (true) {
#         int N, M;
#         cin >> N >> M;
#         if (N == 0 && M == 0) break;

#         int S, D;
#         cin >> S >> D;

#         vector<vector<pair<int, int>>> graph(N);
#         vector<vector<pair<int, int>>> graphS(N);
#         vector<vector<pair<int, int>>> graphD(N);

#         vector<int> dist(N, INF);
#         vector<int> distS(N, INF);
#         vector<int> distD(N, INF);

#         for (int i = 0; i < M; ++i) {
#             int u, v, p;
#             cin >> u >> v >> p;
#             graphS[u].emplace_back(p, v);
#             graphD[v].emplace_back(p, u);
#         }

#         Dijkstra(S, graphS, distS);
#         Dijkstra(D, graphD, distD);

#         int shortest_path = distS[D];
#         for (int u = 0; u < N; ++u) {
#             for (const auto& edge : graphS[u]) {
#                 int w = edge.first;
#                 int v = edge.second;
#                 if (distS[u] + w + distD[v] != shortest_path) {
#                     graph[u].emplace_back(w, v);
#                 }
#             }
#         }

#         Dijkstra(S, graph, dist);
#         cout << (dist[D] != INF ? dist[D] : -1) << endl;
#     }

#     return 0;
# }


'''
7 9
0 6
0 1 1
0 2 1
0 3 2
0 4 3
1 5 2
2 6 4
3 6 2
4 6 4
5 6 1
4 6
0 2
0 1 1
1 2 1
1 3 1
3 2 1
2 0 3
3 0 2
6 8
0 1
0 1 1
0 2 2
0 3 3
2 5 3
3 4 2
4 1 1
5 1 1
3 0 1
0 0
'''