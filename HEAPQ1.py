# https://www.hackerrank.com/challenges/qheap1/problem

import heapq
h = []
heapq.heapify(h)
Q = int(input())

mark = {}
for _ in range(Q):
    query = list(map(int, input().split()))
    if len(query) == 2:
        q, v = query
        if q == 1:
            heapq.heappush(h, v)
        else:
            if v not in mark:
                mark[v] = 1
            else:
                mark[v] += 1
    else:
        while True:
            x = h[0]
            if x in mark:
                heapq.heappop(h)
                mark[x] -= 1
                if mark[x] <= 0: del mark[x]
            else: break
        print(x)

'''
5        
1 4         
1 9         
3           
2 4         
3 
'''