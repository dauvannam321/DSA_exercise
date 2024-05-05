# https://vjudge.net/problem/CodeChef-RRATING
# https://www.onlycode.in/restaurant-rating-solution-heap-codechef-medium/
import heapq
from math import floor 

n = int(input())

max_h = []
min_h = []
heapq.heapify(max_h)
heapq.heapify(min_h)

for _ in range(n):
    line = list(map(int, input().split()))
    
    if len(line) == 2:
        heapq.heappush(max_h, -line[1])

        if (len(min_h) != 0 and -max_h[0] > min_h[0]):
            max_v = max_h[0]
            heapq.heappop(max_h)
            min_v = min_h[0]
            heapq.heappop(min_h)

            heapq.heappush(max_h, -min_v)
            heapq.heappush(min_h, -max_v)
        
        if len(min_h) < floor((len(min_h) + len(max_h))/3):
            heapq.heappush(min_h, -max_h[0])
            heapq.heappop(max_h)

    else:
        if(len(min_h)!=0):
            print(min_h[0])
        else:
            print("No reviews yet") 


'''
10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
2
'''