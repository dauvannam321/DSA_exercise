# https://vjudge.net/problem/UVA-10611

from bisect import bisect_left, bisect_right

n = int(input())
ladies = list(map(int, input().split()))

q = int(input())
queries = list(map(int, input().split()))

def findMaxL(q, ladies):
    l, r = 0, n - 1
    pos = -1
    while (l <= r):
        mid = (l + r)//2
        if ladies[mid] < q:
            pos = mid
            l = mid + 1
        else: 
            r = mid - 1

    return pos

def findMinR(q, ladies):
    l, r = 0, n - 1
    pos = -1
    while (l <= r):
        mid = (l + r)//2
        if ladies[mid] > q:
            pos = mid
            r = mid - 1
        else: 
            l = mid + 1

    return pos


for i in range(q):
    l = findMaxL(queries[i], ladies)
    r = findMinR(queries[i], ladies)

    if l == r == -1:
        print("X", "X")
    elif l == -1:
        print("X", ladies[r])
    elif r == -1:
        print(ladies[l], 'X')
    else:
        print(ladies[l], ladies[r])
'''
4
1 4 5 7
4
4 6 8 10
'''