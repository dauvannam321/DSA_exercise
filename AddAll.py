# https://vjudge.net/problem/UVA-10954

import heapq

while True:
    n = int(input())

    if n==0: break

    a = list(map(int, input().split()))

    heapq.heapify(a)
    # print(a)
    cost = 0
    while len(a) > 1:
        first = heapq.heappop(a)
        # print("F:",first)
        second = heapq.heappop(a)
        # print("S:",second)
        cost += first + second
        # print("Cost: ",cost)
        heapq.heappush(a, first + second)
        # print("A:",a)
        

    print(cost)

