# https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/practice-problems/algorithm/monk-and-multiplication/
# https://www.geeksforgeeks.org/max-heap-in-python/

import heapq

n = int(input())
A = list(map(int, input().split()))

h = []
heapq.heapify(h)
for x in A:
    heapq.heappush(h, -x)
    if len(h) < 3:
        # print(h)
        print(-1)
    else:
        # print("*" * 10)
        # print(h)
        first = heapq.heappop(h)
        second = heapq.heappop(h)
        third = heapq.heappop(h)
        # print(first)
        # print(second)
        # print(third)
        print(-1 * first * second * third)
        heapq.heappush(h, first)
        heapq.heappush(h, second)
        heapq.heappush(h, third)
        # print(h)
        # print("*" * 10)


