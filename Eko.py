# https://vjudge.net/problem/SPOJ-EKO
# IgnacioLiberon's solution for [SPOJ-EKO]
def cut(trees, m):
	total = 0
	for tree in trees:
		if tree > m:
			total += tree - m
	return total

def find_height(trees, m):
	min_h = 0
	max_h = max(trees)

	while min_h <= max_h:
		mid_h = (max_h + min_h)//2
		wood = cut(trees, mid_h)

		if wood == m: return mid_h
		elif wood > m: min_h = mid_h + 1 
		else: max_h = mid_h - 1
	
	return max_h
n, m = map(int, input().split())

trees = list(map(int, input().split()))
print(find_height(trees, m))