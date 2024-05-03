# https://vjudge.net/problem/SPOJ-PRO

import heapq

n = int(input())
max_h = []
min_h = []
heapq.heapify(max_h)
heapq.heapify(min_h)

cost = 0

total_receipt = 0
used = [False] * 10 ** 6
id = 0
for _ in range(n):
    receipts = list(map(int, input().split()))[1:]

    for i in receipts:
        heapq.heappush(max_h, (-i, id))
        heapq.heappush(min_h, (i, id))
        id += 1

    # max_val = heapq.heappop(max_h)
    # min_val = heapq.heappop(min_h)
    while used[max_h[0][1]]:
        heapq.heappop(max_h)
    while used[min_h[0][1]]:
        heapq.heappop(min_h)
    used[max_h[0][1]] = True
    used[min_h[0][1]] = True
    cost += -max_h[0][0] - min_h[0][0]
    heapq.heappop(max_h)
    heapq.heappop(min_h)
    # print(max_val)
    # print(min_val)
    # cost += max_val - min_val
    # max_h.remove(-min_val)
    # min_h.remove(max_val)
print(cost)

'''
5
3 1 2 3
2 1 1
4 10 5 5 1
0
1 2
'''