# https://codeforces.com/problemset/problem/424/B

from math import sqrt
import heapq

standard_population = int(1e6)
n, s = map(int, input().split())


min_r = int(1e6 + 1)

dis = []

for _ in range(n):
	x, y, k = map(int, input().split())
	heapq.heappush(dis, (sqrt(x ** 2 + y ** 2), k))

# print(dis)

while dis:
	r, population = heapq.heappop(dis)
	s += population
	if s >= standard_population: 
		min_r = r
		break
# print(s)
# print(standard_population)
if s >= standard_population: print("{:.7f}".format(min_r))
else: print(-1)