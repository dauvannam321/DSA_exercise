# https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/monk-and-his-friends/

T = int(input())

for _ in range(T):
	N, M = map(int, input().split())

	students = list(map(int, input().split()))
	st_before = set(students[:N])
	st_after = students[N:]
	
	for i in st_after:
		if i in st_before:
			print("YES")
		else:
			st_before.add(i)
			print("NO")