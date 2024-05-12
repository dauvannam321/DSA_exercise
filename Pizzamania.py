# https://vjudge.net/problem/SPOJ-OPCPIZZA

from sys import stdin

t = int(stdin.readline())

for _ in range(t):
	n, m = list(map(int, stdin.readline().split()))

	moneys = list(map(int, stdin.readline().split()))

	# print(moneys)
	count = 0
	pairs = {}

	for money in moneys:
		if money in pairs:
			count+=1
			pairs[money] -= 1
			if pairs[money] == 0:
				pairs.pop(money)

		else:
			if m - money in pairs:
				pairs[m - money] += 1
			else:
				pairs[m - money] = 1

	print(count)