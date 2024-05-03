# https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/practice-problems/algorithm/roy-and-trending-topics-1/

# Each contains 6 space separated numbers representing 
# Topic ID,
# current z-score - Z, 
# Posts - P, 
# Likes - L, 
# Comments - C, 
# Shares - S
import heapq

n = int(input())
h = []

for _ in range(n):
    id, z, p, l, c, s = map(int, input().split())
    h.append((-(p * 50 + l * 5 + c * 10 + s * 20 - z), id, z))

heapq.heapify(h)
# print(h)
res = []
for _ in range(5):
    res.append(heapq.heappop(h))

# res = sorted(res, key=lambda x: (x[0], -x[1]))
# print(res[-1])
for i in h:
    if i[0] == res[0][0] or i[0] == res[-1][0]:
        res.append(i)

# print(res)
res = sorted(res, key=lambda x: (x[0], -x[1]))
# print(res)
for i in range(5):
    print(res[i][1], res[i][2] - res[i][0])


# for _ in range(5):
#     heapq.heappop(h)
#     print(h)
