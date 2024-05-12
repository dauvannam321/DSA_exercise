from sys import stdin

case = 1

def BinarySearchFirst(array, left, right, x):
	if left <= right:
		mid = (left + right)//2
		if (mid == left or x != array[mid - 1]) and array[mid] == x:
			return mid
		elif(x > array[mid]):
			return BinarySearchFirst(array, mid + 1, right, x)
		else:
			return BinarySearchFirst(array, left, mid - 1, x)
		
	return -1

while True:
	N, Q = list(map(int, stdin.readline().split()))
	if N == 0 and Q == 0: 
		break

	marbles = []

	for _ in range(N):
		marbles.append(int(stdin.readline()))

	marbles.sort()

	left = 0
	right = len(marbles) - 1
	print("CASE# {}:".format(case))
	for _ in range(Q):
		x = int(stdin.readline())
		query = BinarySearchFirst(marbles, left, right, x)
		if query != -1:
			print("{} found at {}".format(x, query + 1))
		else:
			print("{} not found".format(x))

	case += 1

'''
4 1
2
3
5
1
5
5 2
1
3
3
3
1
2
3
0 0
'''
	